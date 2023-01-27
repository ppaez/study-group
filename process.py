import csv


def load(csv_file_name):
    "Load csv_file and return a list of dicts."
    with open(csv_file_name, newline="", encoding="latin1") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)
