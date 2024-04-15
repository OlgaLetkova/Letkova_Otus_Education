import csv

from files import DATA_RESOURCES_CSV_FILE_PATH


def read_lines_from_csv(limit=100, source_file=DATA_RESOURCES_CSV_FILE_PATH):
    result = []
    with open(source_file, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
            if len(result) == limit:
                break
    return result
