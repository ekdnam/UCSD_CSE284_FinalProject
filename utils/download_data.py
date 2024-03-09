# Download data files to data/ folder

import os
import requests
from zipfile import ZipFile

# Data directory relative to utils
parent_dir = os.getcwd()
data_dir = os.path.join(parent_dir, "data")

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)


def download_and_extract(name, study, link):
    # Determine the path for the file
    path_dir = os.path.join(data_dir, study)
    os.makedirs(path_dir, exist_ok=True)

    file_extension = os.path.splitext(link)[-1]
    local_filename = os.path.join(path_dir, name + file_extension)

    local_filename = os.path.join(path_dir, name + os.path.splitext(link)[-1])
    if os.path.exists(local_filename):
        print(f"{name} already exists. Skipping download.")
        return
    else:
        # Download the file
        print(f"Downloading {link}...")
        response = requests.get(link)
        response.raise_for_status()  # This will raise an error for bad responses

        # Save the file to the specified path
        with open(local_filename, "wb") as f:
            f.write(response.content)
        print(f"Saved {name} to {local_filename}")

    # Only create a directory and extract if it's a ZIP file
    if file_extension == ".zip":
        zip_dir = os.path.join(path_dir, name)
        if not os.path.exists(zip_dir):
            os.makedirs(zip_dir, exist_ok=True)
            with ZipFile(local_filename, "r") as zip_ref:
                zip_ref.extractall(zip_dir)
            print(f"Extracted {name}")
        else:
            print(f"{name} extraction directory already exists. Skipping extraction.")


"""BMI Dataset

Genome-Wide Association Study in 3,173 Outbred Rats Identifies Multiple Loci for Body Weight, Adiposity, and Fasting Glucose

https://library.ucsd.edu/dc/object/bb9156620z

https://pubmed.ncbi.nlm.nih.gov/32860487/

https://library.ucsd.edu/dc/object/bb9156620z

"""

bmi_links = {
    "readme": "https://library.ucsd.edu/dc/object/bb9156620z/_1_1.txt",
    "phenotype_data": "https://library.ucsd.edu/dc/object/bb9156620z/_2_1.zip",
    "ld_pruned_genotype_data": "https://library.ucsd.edu/dc/object/bb9156620z/_3_1.zip",
    "genetic_relatedness_matrix": "https://library.ucsd.edu/dc/object/bb9156620z/_5_1.zip",
    "gwas_summary_files": "https://library.ucsd.edu/dc/object/bb9156620z/_6_1.zip",
}

for name, link in bmi_links.items():
    download_and_extract(name, "bmi", link)


"""Psychiatric Dataset

https://cgord.org/dataset/1

https://pubmed.ncbi.nlm.nih.gov/35237186/

"""
