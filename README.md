# CSE284 Final Project: Polygenic Risk Score Analysis on Rat Models

**Group 23**

- Vince Rothenberg 

- Aditya Mandke 

- Tiffany Chu 

## Overview

This repository hosts the code and analysis for the final project conducted for the CSE 284: Personal Genomics course at UCSD, Winter 2024. Our project focuses on leveraging Genome-Wide Association Study (GWAS) datasets to infer Polygenic Risk Scores (PRS) for various traits, specifically utilizing a BMI dataset obtained from a comprehensive study on 3,173 outbred rats.

The primary aim of this project is to use GWAS summary statistics from the aforementioned study to infer polygenic risk scores (PRS) for various psychiatric disorders in rats, based on the genotypes provided in the BMI study. We will explore correlations, common genes, and other significant findings to understand the genetic underpinnings of these traits better.

## Dataset

The core dataset for this project comes from a Genome-Wide Association Study (GWAS) that identified multiple loci for body weight, adiposity, and fasting glucose in 3,173 outbred rats.

- **Study Citation**: Chitre, A. S., Polesskaya, O., Holl, K., Gao, J., Cheng, R., Bimschleger, H., Garcia Martinez, A., George, T., Gileta, A. F., Han, W., Horvath, A., Hughson, A., Ishiwari, K., King, C. P., Lamparelli, A., Versaggi, C. L., Martin, C., St. Pierre, C. L., Tripi, J. A., … Palmer, Abraham A.,Solberg Woods, L. C. (2022). Data from: Genome‐Wide Association Study in 3,173 Outbred Rats Identifies Multiple Loci for Body Weight, Adiposity, and Fasting Glucose. UC San Diego Library Digital Collections. [DOI: 10.6075/J0Q240F0](https://doi.org/10.6075/J0Q240F0).
- 
## Methodology

1. **Polygenic Risk Score Calculation**: Utilizing GWAS summary statistics, we calculate PRS for individual genomes within our dataset, focusing on traits with robust genetic signals.
2. **Analysis**: We will conduct an in-depth analysis to find correlations between PRS for psychiatric disorders and BMI-related traits. This includes examining common genes and loci that contribute to both sets of traits.
3. **Validation and Benchmarking**: We aim to validate our findings through comparative analysis and benchmarking against known datasets and literature.

## Installation

This project relies on a Conda environment for managing dependencies. Follow these steps to set up your environment:

1. **Install Miniconda or Anaconda**: If you haven't already, install Miniconda or Anaconda to manage your environments. You can find installation instructions here: [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual).

2. **Clone the Repository**: Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/ekdnam/UCSD_CSE284_FinalProject.git
   cd UCSD_CSE284_FinalProject
   ```

3. **Install the Packages**: Ensure you have already installed the following Python packages.
   ```
   matplotlib
   numpy
   pandas
   seaborn
   requests
   scipy
   ```

## File structure

```

├── Discussion.md
├── LICENSE
├── README.md
├── analysis
│   ├── bmi.ipynb
│   ├── generate_r2.ipynb
│   ├── prscs.ipynb
│   ├── test.txt
│   ├── test_plink_on_oft.ipynb
│   └── test_prsice_on_oft.ipynb
├── data
│   ├── bmi
│   │   ├── genetic_relatedness_matrix
│   │   │   ├── obesity_published_grm.grm.N.bin
│   │   │   ├── obesity_published_grm.grm.bin
│   │   │   └── obesity_published_grm.grm.id
│   │   ├── genetic_relatedness_matrix.zip
│   │   ├── gwas_summary_files
│   │   │   ├── gemma_commands.sh
│   │   │   ├── physiological_bmi_bodylength_w_tail.csv
│   │   │   ├── physiological_bmi_bodylength_wo_tail.csv
│   │   │   ├── physiological_bodylength_w_tail.csv
│   │   │   ├── physiological_bodylength_wo_tail.csv
│   │   │   ├── physiological_bodyweight.csv
│   │   │   ├── physiological_epifat.csv
│   │   │   ├── physiological_fasting_glucose.csv
│   │   │   ├── physiological_parafat.csv
│   │   │   └── physiological_retrofat.csv
│   │   ├── gwas_summary_files.zip
│   │   ├── ld_pruned_genotype_data
│   │   │   ├── LD_pruned_0.95
│   │   │   │   ├── chr1.round2_impute2_3473.bimbam
│   │   │   │   ├── chr10.round2_impute2_3473.bimbam
│   │   │   │   ├── chr11.round2_impute2_3473.bimbam
│   │   │   │   ├── chr12.round2_impute2_3473.bimbam
│   │   │   │   ├── chr13.round2_impute2_3473.bimbam
│   │   │   │   ├── chr14.round2_impute2_3473.bimbam
│   │   │   │   ├── chr15.round2_impute2_3473.bimbam
│   │   │   │   ├── chr16.round2_impute2_3473.bimbam
│   │   │   │   ├── chr17.round2_impute2_3473.bimbam
│   │   │   │   ├── chr18.round2_impute2_3473.bimbam
│   │   │   │   ├── chr19.round2_impute2_3473.bimbam
│   │   │   │   ├── chr2.round2_impute2_3473.bimbam
│   │   │   │   ├── chr20.round2_impute2_3473.bimbam
│   │   │   │   ├── chr3.round2_impute2_3473.bimbam
│   │   │   │   ├── chr4.round2_impute2_3473.bimbam
│   │   │   │   ├── chr5.round2_impute2_3473.bimbam
│   │   │   │   ├── chr6.round2_impute2_3473.bimbam
│   │   │   │   ├── chr7.round2_impute2_3473.bimbam
│   │   │   │   ├── chr8.round2_impute2_3473.bimbam
│   │   │   │   └── chr9.round2_impute2_3473.bimbam
│   │   │   ├── LD_pruned_0.95.zip
│   │   │   ├── LD_pruned_PLINK
│   │   │   │   ├── P50_round2_LD_pruned_3473.bed
│   │   │   │   ├── P50_round2_LD_pruned_3473.bim
│   │   │   │   └── P50_round2_LD_pruned_3473.fam
│   │   │   └── LD_pruned_PLINK.zip
│   │   ├── ld_pruned_genotype_data.zip
│   │   ├── phenotype_data
│   │   │   ├── Obesity_normalized_phenotypes_n3173.csv
│   │   │   ├── Obesity_published_phenotypes_raw_n3173.csv
│   │   │   └── trait_ontology.xlsx
│   │   ├── phenotype_data.zip
│   │   └── readme.txt
│   └── oft
│       ├── description.csv
│       └── phenotypes.csv
├── run_preliminary_analysis.sh
├── scripts
│   ├── generate_pvals.sh
│   ├── generate_valid_data.sh
│   └── prs_scoring.sh
├── test.md
├── train
└── utils
    ├── download_data.py
    ├── generate_r2.py
    └── write_prs_files.py
```

## Usage

Run download_data.py which will pull GWAS datasets from the studies.

```bash
python utils/download_data.py
```

After this, unzip `data/bmi/ld_pruned_genotype_data/LD_pruned_PLINK.zip` to `data/bmi/ld_pruned_genotype_data/`.

Now, run
```bash
python utils/write_prs_files.py
```

This writes the prs files for all the phenotypes we have to `./prs`.

Now, execute
```bash
$ chmod +x scripts/generate_pvals.sh
$ chmod +x scripts/generate_valid_data.sh
$ chmod +x scripts/prs_scoring.sh

$ ./scripts/generate_pvals.sh
$ ./scripts/generate_valid_data.sh
$ ./scripts/prs_scoring.sh
```

This generates the pvals, valid data, and runs the prs scoring using plink.

Finally, run
```bash
python utils/generate_r2.py
```

This generates the r2 scores for each phenotype and stores the best p values for each to a csv.

## Analysis Scripts

### [bmi.ipynb](./analysis/bmi.ipynb)

It facilitates the analysis of Genome-Wide Association Study (GWAS) data related to Body Mass Index (BMI) and body length with tail. The script utilizes a variety of visualization techniques to offer insights into genetic associations within the dataset.

This Python script facilitates the analysis of Genome-Wide Association Study (GWAS) data related to Body Mass Index (BMI) and body length with tail. The script utilizes various visualization techniques to offer insights into genetic associations within the dataset.

- **Data Loading**: The script loads BMI-related data from a CSV file using Pandas, providing easy access to the dataset for further analysis.

- **Visualization Techniques**:
  - **Histogram of Wald Test p-values**: Illustrates the distribution of significance levels obtained from the Wald test using logarithmic scaling.
  - **Distribution of Allele Frequency**: Seaborn is used to create a histogram showing the distribution of allele frequencies, aiding in understanding genetic variation.
  - **Distribution of Effect Sizes**: Visualizes the distribution of effect sizes using a histogram, revealing the strength of associations between genetic variants and BMI.
  - **Distribution of p-values (-log10 transformed)**: A plot of negative logarithm-transformed p-values highlights significant associations in the dataset.
  - **Manhattan Plot**: Displays the genomic locations of significant associations, with each point representing a SNP color-coded by chromosome. A red dashed line indicates the Bonferroni-corrected significance threshold.
  - **QQ Plot of GWAS P-values**: Evaluates the deviation of observed p-values from the expected distribution under the null hypothesis, aiding in dataset quality assessment.

### [prscs.ipynb](./analysis/prscs.ipynb)

Helps handle and analyze SNP data.

- **Data Loading**: Easily load SNP data from files.
- **Calculate MAF**: Compute Minor Allele Frequency (MAF) to understand allele prevalence.
- **Filter SNPs**: Identify and save SNPs with rare minor alleles for further analysis.
- **Access Thousand Genomes Data**: Explore genetic information from the Thousand Genomes project.

This script serves as a valuable resource for researchers and enthusiasts working with genetic data for BMI research.

### [test_plink_on_oft.ipynb](./analysis/test_plink_on_oft.ipynb)

### Phenotype Analysis Overview

This Jupyter notebook is dedicated to analyzing OFT phenotypic data from the './data/oft/phenotypes.csv' file. Here's a brief summary of its key functionalities:

- **Data Loading**: Phenotypic data is loaded from the './data/oft/phenotypes.csv' file using Pandas, enabling efficient data manipulation and analysis.

- **Phenotype-PRS Correlation**: The notebook iterates over each phenotype column in the dataset, calculates the Pearson correlation coefficient between the phenotype and Polygenic Risk Scores (PRS) obtained from './prsice_data/PRSice_custom_pvalue.best', and computes the coefficient of determination (R-squared) to quantify the strength of the relationship.

- **Results Presentation**: For each phenotype, the notebook displays the phenotype name along with its corresponding R-squared value, providing insights into the degree of association between the phenotype and PRS.

### [test_prsice_on_oft.ipynb](./analysis/test_prsice_on_oft.ipynb)

It has more or less the same funcitonalities as above. It tests the prsice outputs against OFT phenotypes.

## Contact

For any inquiries or contributions to the project, please contact:

- Vince Rothenberg [vrothenberg (at) ucsd.edu]
- Aditya Mandke [amandke (at) ucsd.edu]
- Tiffany Chu [t2chu (at) health.ucsd.edu]

## Acknowledgments

We would like to thank the authors of the original BMI dataset study for making their data available for academic research, as well as the instructors and TA's of CSE 284 at UCSD for their guidance and support throughout this project.

## License

This project is licensed under the Apache 2.0 license
