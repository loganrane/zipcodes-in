import csv

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