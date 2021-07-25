import json
from pprint import pprint
from internal_utils import (parseCSV)


def main():
    SCHEMA = {
        "zipcode" : {"public": "zipcode"},
        "region": {"public": "region"},
        "state_ut": {"public": "state_ut"},
        "country": {"public": "country"},
        "latitude": {"public": "latitude"},
        "longitude": {"public": "longitude"},
        "post_office": {"public": "post_office"},
    }

    databaseFileName = ".\data\zipcode_db.csv"
    baseData = parseCSV(databaseFileName)
    
    with open("..\zipcode_script\zips.json", "w") as f:
        json.dump(baseData, f)


if __name__ == "__main__":
    main()