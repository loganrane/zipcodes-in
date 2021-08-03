import re
from collections import Counter
import json
from zipcode import Zipcode
from pprint import pprint

with open('.\\zips.json', 'rb') as f:
    data = json.load(f)


def filterByLocation(query):
    matching_locations = []
    for zipcode in data:
        if zipcode['region'] == query or zipcode['state_ut'] == query or zipcode['country'] == query:
            matching_locations.append(zipcode)

    return matching_locations


def similarToZipcode(query):
    matching_locations = []
    for zipcode in data:
        if zipcode['zipcode'].startswith(query):
            matching_locations.append(zipcode)

    return matching_locations

# Rancki -> Ranchi -> filterByLocation(Ranchi) -> all the locations having ranchi as either, region or city or country
# Rancki -> Ranch -> filterByLocation(Ranch) ->

# {'MP': 'Madhya Pradesh', 'AP'}


hello = list()
for zipcode in data:
    hello.append(zipcode['region'])
    hello.append(zipcode['state_ut'])
    hello.append(zipcode['country'])

hello = list(hello)

WORDS = Counter(hello)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]

    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


# Sorting wrapper for getting the max value
def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)
