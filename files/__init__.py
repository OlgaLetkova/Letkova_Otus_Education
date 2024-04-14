import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


TXT_FILE_PATH = get_path(filename="sub_breeds.txt")
CSV_FILE_PATH = get_path(filename="data_resources.csv")

