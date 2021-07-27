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
        self._basePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zips.json')

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

        if len(zipcode) != self._validLen:
            raise ValueError(
                "Invalid Format, zipcode must be of the format: XXXXXX")

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

    @_cleanZipcode
    def matching(self, zipcode):
        """Return the data of matching zipcode"""
        return [data for data in self._baseData if data['zipcode'] == zipcode]

    @_cleanZipcode
    def validate(self, zipcode):
        return bool(self.matching(zipcode))