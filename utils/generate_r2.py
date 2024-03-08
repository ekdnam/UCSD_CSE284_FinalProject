"""
Module: generate_r2.py
Author: Aditya Mandke
Description:
    This module contains functions to analyze polygenic risk scores (PRS) for 
    various physiological traits. It includes functionality to calculate the 
    best p-values for PRS calculation based on the highest R-squared value between 
    the phenotype and PRS, and to perform subsequent analysis on the PRS data.
"""
import pandas as pd
import scipy.stats

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

prs2col = {
    "bodylength_w_tail": "length_w_tail_cm",
    "parafat": "parametrial_fat_weight_g",
    "bmi_bodylength_wo_tail": "bmi_wo_tail",
    "bodyweight": "body_weight_g",
    "retrofat": "retroperitoneal_fat_weight_g",
    "bmi_bodylength_w_tail": "bmi_w_tail",
    "epifat": "epididymis_fat_weight_g",
    "bodylength_wo_tail": "length_wo_tail_cm",
    "fasting_glucose": "glucose_reading_mg_dl",
}


def find_best_pvalues(verbose=False):
    """
    Find the best p-values for each phenotype based on the highest R-squared value.

    This function iterates through a list of phenotype filenames and determines the best p-value
    that yields the highest R-squared value when calculating the correlation between the phenotype
    and the polygenic risk scores (PRS). It reads PRS and phenotype data files, computes the
    correlation coefficient (Pearson's r), and squares it to obtain the R-squared value.

    Returns:
    dict: A dictionary containing the best p-value and corresponding R2 value for each phenotype.
    """
    out_dir = "out"
    phenotype_data_path = (
        "./data/bmi/phenotype_data/Obesity_normalized_phenotypes_n3173.csv"
    )
    best_p = {}

    # Iterate through each phenotype file
    for fname in filenames:
        if verbose:
            print(f"Processing {fname}")
        p_max = (
            None  # Initialize variables to track the best p-value and R-squared value
        )
        r2_max = None
        input_file_template = f"./{out_dir}/{file2prs[fname]}/{file2prs[fname]}"

        # Iterate through a predefined list of p-values
        for pval in ["0.000001", "0.00001", "0.0001", "0.001", "0.05", "0.1"]:
            # Read PRS and phenotype data files
            prs = pd.read_csv(
                f"{input_file_template}.{pval}.profile", delim_whitespace=True
            )
            phen = pd.read_csv(phenotype_data_path)

            # Select relevant columns and rename them for consistency
            phen = phen[["rat_rfid", prs2col[file2prs[fname]]]]
            phen = phen.rename(
                columns={"rat_rfid": "IID", prs2col[file2prs[fname]]: "phen"}
            )
            phen = phen.dropna()  # Remove rows with missing values

            # Merge PRS and phenotype data on the shared column 'IID'
            merged_df = pd.merge(prs, phen, on=["IID"])

            # Compute the correlation coefficient (Pearson's r) and square it to obtain R-squared
            curr_r2 = (
                scipy.stats.pearsonr(merged_df["phen"], merged_df["SCORE"])[0] ** 2
            )
            if verbose:
                print(f"pval: {pval}\tcurr_r2: {curr_r2}")

            # Update the best p-value and R-squared value if necessary
            if r2_max is None:
                r2_max = curr_r2
                p_max = pval
            else:
                if curr_r2 > r2_max:
                    r2_max = curr_r2
                    p_max = pval
        if verbose:
            print(f"MAX_P: {p_max}")
            print()
        # Store the best p-value and corresponding R-squared value for the current phenotype
        best_p[fname] = [p_max, r2_max]

    return best_p


# Execute the function to find the best p-values for each phenotype
best_p_values = find_best_pvalues(verbose=True)

# Print the results
for name, values in best_p_values.items():
    print(f"Best p-value for {name}: {values[0]}, R-squared: {values[1]}")
