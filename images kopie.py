import wget
import os
import os.path
import zipfile

def download_resources():
    if not os.path.isdir("resources/fonts"):
        url = "https://www.dropbox.com/s/3wcp26el8x5na4j/resources.zip?dl=1"

        print("Dowloading resources...")
        wget.download(url)

        print("\nExtracting resources...")
        zip_ref = zipfile.ZipFile("resources.zip", 'r')
        zip_ref.extractall(".")
        zip_ref.close()

        print("Cleaing up...")
        os.remove("resources.zip")

        print("Resources downloaded successfully.")

download_resources()
