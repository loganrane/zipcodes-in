"""
Zipcode India
-----------------------------

Zipcode class to validate and fetch details of India zipcodes
"""
import json
import os
import sys
import warnings
import random


class Zipcode():
    """Zipcode Class"""

    def __init__(self):
        """Constructor to initialze the path, data and valid length."""
        self._validLen = 6
        self._basePath = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'zips.json')

        with open(self._basePath, "rb") as f:
            self._baseData = json.load(f)

    def __repr__(self):
        """Print the description when print(obj) is called."""
        return f'Zipcode class to validate and fetch data of provided India zipcode'

    def _cleanZipcode(function):
        """Decorator to clean the zipcode"""

        def wrapper(self, zipcode, *args, **kwargs):
            if zipcode is None or isinstance(zipcode, str) is False:
                raise TypeError("Invalid Type, zipcode must be a string")

            cleanZip = self._clean(zipcode)
            res = function(self, cleanZip, *args, **kwargs)

            return res
        return wrapper

    def _clean(self, zipcode):
        """Remove whitespaces and check the length, format and character."""
        zipcode = zipcode.strip()

        if len(zipcode) > self._validLen:
            raise ValueError(
                "Invalid Format, zipcode must be of the format: XXXXXX for hard search and any less character for soft search")

        if not zipcode.isnumeric():
            raise ValueError(
                "Invalid characters, zipcode may only contain digits")

        return zipcode

    def listTopN(self, N):
        """Return the first N entries"""
        return self._baseData[:N]

    def listAll(self):
        """Return whole dataset"""
        return self._baseData

    def random(self):
        """Return a random entry"""
        idx = random.randint(0, len(self._baseData))
        return self._baseData[idx]

    def listRandomN(self, N):
        """Return a list of N random entries"""
        if N > 100:
            raise ValueError(
                "Please enter N <= 100 or use listAll to get all data")
        idx = random.sample([i for i in range(0, len(self._baseData))], N)
        res = [self._baseData[i] for i in idx]

        return res

    def filterByLocation(self, query):
        """Filter the locations by region, state or country
           Doesn't differentiate matching names in region and state yet"""
        matching_locations = []
        for zipcode in self._baseData:
            if zipcode['region'] == query or zipcode['state_ut'] == query or zipcode['country'] == query:
                matching_locations.append(zipcode)

        return matching_locations

    @_cleanZipcode
    def similarToZipcode(self, query):
        """Return the locations which has a prefix same as provided query"""
        matching_locations = []
        for zipcode in self._baseData:
            if zipcode['zipcode'].startswith(query):
                matching_locations.append(zipcode)

        return matching_locations

    @_cleanZipcode
    def matching(self, zipcode, soft=False):
        """Return the data of matching zipcode"""
        if soft == True:
            # Truncuate the zipcode to 4 letters for soft search
            zipcode = zipcode[:min(4, len(zipcode))]
            return self.similarToZipcode(zipcode)

        return [data for data in self._baseData if data['zipcode'] == zipcode]

    @_cleanZipcode
    def validate(self, zipcode):
        return bool(self.matching(zipcode))
