import os

def get_latest_version(files):

    files.sort(reverse=True)

    return files[0]
