import csv
import time

def parseCSV(filename):
    """Read a CSV (Comma Seperated file) and convert to list of dictionaries.
    @params:
        filename: location of the CSV file (relative to project root)(str)
    @return:
        list of dictionaries for each row"""
    with open(filename) as f:
        return [
            {key: value for key, value in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)
        ]


# def stripEmptyKeys(base, schema):
#     """Strip keys from the base data if not in schema
#     @params:
#         base: base data read from the CSV file
#         schema: schema of the database
#     @return:
#         list of dictionaries with keys stripped which are not in schema"""

#     return [
#         {key: value for key, value in place.items() if key in schema}
#         for place in base
#     ]