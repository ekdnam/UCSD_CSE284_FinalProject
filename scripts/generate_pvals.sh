#!/bin/bash

# Script: generate_pvals.sh
# Author: Aditya Mandke
# Description: This script generates pvals files from the specified input files.
#              It removes any existing 'pvals' directory, creates a new one,
#              and then generates pvals files for each input file.
# Usage: bash generate_pvals.sh

# Print current working directory
# pwd

prs_dir=prs
pvals_dir=pvals

# Remove 'pvals' directory if it exists
echo "removing pvals directory (if it exists)"
rm -rf $pvals_dir

# Create 'pvals' directory
echo "creating pvals directory"
mkdir $pvals_dir

# Define list of filenames
filenames=(
    'bodylength_w_tail'
    'parafat'
    'bmi_bodylength_wo_tail'
    'bodyweight'
    'retrofat'
    'bmi_bodylength_w_tail'
    'epifat'
    'bodylength_wo_tail'
    'fasting_glucose'
)

# Iterate over each filename
for filename in "${filenames[@]}"; do
    echo "generate pvals for $filename"
    cat "$prs_dir/prs_${filename}_profile.txt" | awk 'NR!=1{print $2 "\t" $9}' > "$pvals_dir/${filename}.pvals"
done