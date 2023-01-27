from urllib.request import urlopen
from urllib.request import Request
from zipfile import ZipFile


def download(url, output_file):
    "Get data from url and store in output_file."
    request = Request(url)
    request.add_header("User-Agent", "urllib")
    response = urlopen(request)
    data = response.read()
    with open(output_file, "wb") as f:
        f.write(data)


def extract(zip_file, output_folder):
    "Extract all CSV files from zip_file into output_folder."
    zip = ZipFile(zip_file)
    zip.extractall(path="csv")
