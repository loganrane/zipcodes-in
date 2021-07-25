import json
from pprint import pprint

from internal_utils import (parseCSV)

def main():
    SCHEMA = {
        "zipcode" : {"public": "zipcode"},
        "region": {"public": "region"},
        "state": {"public": "state"},
        "country": {"public": "country"},
        "latitude": {"public": "lat"},
        "longitude": {"public": "long"},
        "population": {"public": "population"},
    }

    databaseFileName = ".\data\zipcode_db.csv"
    baseData = parseCSV(databaseFileName)

    print("writing zipcode information for {} places".format(len(baseData)))
    
    with open("zips.json", "w") as f:
        json.dump(baseData, f)

    pprint(baseData)


if __name__ == "__main__":
    main()