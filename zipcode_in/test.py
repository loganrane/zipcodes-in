import json
from zipcode import Zipcode

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


def similarToLocation():
    # Will take some time to implement
    pass
