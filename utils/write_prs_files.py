"""
Script: generate_prs_profiles.py
Author: Aditya Mandke
Description: This script processes GWAS (Genome-Wide Association Study) summary files
             to generate PRS (Polygenic Risk Score) profiles in a standardized format.
             It reads CSV files containing GWAS summary data for various physiological traits,
             transforms the data into the required format, and saves PRS profiles in the 'prs'
             directory. The PRS profiles include information such as chromosome (CHR),
             SNP identifier (SNP), base pair position (BP), effect allele (A1),
             statistical test type (TEST), sample size (NMISS), effect size (BETA),
             test statistic (STAT), and p-value (P).
Usage: python generate_prs_profiles.py
"""

import os
import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Specify the directory path
DIRECTORY = "./prs"

# Create the directory if it doesn't exist
os.makedirs(DIRECTORY, exist_ok=True)


def get_snp_data_in_format(text):
    """
    Convert SNP data to the required format.

    Parameters:
    text (str): Input SNP data in the format "chr:position:allele1:allele2".

    Returns:
    str: SNP data in the format "rs[position]".
    """
    return "rs" + text.split(":")[1]


def get_chromo(text):
    """
    Extract chromosome information from SNP data.

    Parameters:
    text (str): Input SNP data in the format "chr:position:allele1:allele2".

    Returns:
    str: Chromosome information extracted from the input SNP data.
    """
    return text[3:]


# List of filenames representing physiological traits
filenames = [
    "physiological_bodylength_w_tail",
    "physiological_parafat",
    "physiological_bmi_bodylength_wo_tail",
    "physiological_bodyweight",
    "physiological_retrofat",
    "physiological_bmi_bodylength_w_tail",
    "physiological_epifat",
    "physiological_bodylength_wo_tail",
    "physiological_fasting_glucose",
]

# Dictionary mapping filenames to their corresponding PRS profile names
file2prs = {
    "physiological_bodylength_w_tail": "bodylength_w_tail",
    "physiological_parafat": "parafat",
    "physiological_bmi_bodylength_wo_tail": "bmi_bodylength_wo_tail",
    "physiological_bodyweight": "bodyweight",
    "physiological_retrofat": "retrofat",
    "physiological_bmi_bodylength_w_tail": "bmi_bodylength_w_tail",
    "physiological_epifat": "epifat",
    "physiological_bodylength_wo_tail": "bodylength_wo_tail",
    "physiological_fasting_glucose": "fasting_glucose",
}

# Process each file to generate PRS profile
for name in filenames:
    input_filename = f"data/bmi/gwas_summary_files/{name}.csv"
    output_filename = f"./prs/prs_{file2prs[name]}_profile.txt"
    logging.info("Processing %s: %s", name, input_filename)

    # Read the CSV file containing GWAS summary data
    data = pd.read_csv(input_filename)

    # Rename columns for consistency with PRS profile format
    data.rename(
        columns={
            "chr": "CHR",
            "rs": "SNP",
            "ps": "BP",
            "allele1": "A1",
            "n_miss": "NMISS",
            "beta": "BETA",
            "p_score": "P",
            "se": "STAT",
        },
        inplace=True,
    )

    # Add a column for the type of statistical test performed
    data["TEST"] = "ADD"

    # Apply formatting functions to certain columns
    data["CHR"] = data["CHR"].apply(get_chromo)

    # Select relevant columns for PRS profile
    prs_data = data[["CHR", "SNP", "BP", "A1", "TEST", "NMISS", "BETA", "STAT", "P"]]

    # Save PRS profile as a tab-separated file in the 'prs' directory
    prs_data.to_csv(
        f"./{DIRECTORY}/prs_{file2prs[name]}_profile.txt", sep="\t", index=False
    )
    logging.info("PRS for %s written to %s", name, output_filename)
