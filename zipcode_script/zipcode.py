"""
Zipcode India
-----------------------------

Zipcode class to validate and fetch details of India zipcodes
"""
import json
import os
import sys
import warnings

class Zipcode():
    """Zipcode Class"""
    def __init__(self):
        """Constructor to initialze the path, data and valid length."""
        self._validLen = 6
        self._basePath = os.path.join(os.path.abspath("."), 'zips.json')
        self._baseData = json.load(self._basePath)

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

    def _clean(zipcode):
        """Remove whitespaces and check the length, format and character."""
        zipcode = zipcode.strip()
        if len(zipcode) != self._validLen:
            raise ValueError("Invalid Format, zipcode must be of the format: XXXXXX")
        
        if not zipcode.isnumeric():
            raise ValueError("Invalid characters, zipcode may only contain digits")
        
        return zipcode
