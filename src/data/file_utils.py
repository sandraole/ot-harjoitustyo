# data/file_utils.py
import os


def open_for_write(file_path, encoding="utf-8"):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            print(f"Could not create directory {directory}: {e}")

    # palautetaan file-objekti, jota voi käyttää with-openissa
    return open(file_path, "w", encoding=encoding)
