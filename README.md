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


## Contact

For any inquiries or contributions to the project, please contact:

- Vince Rothenberg [vrothenberg (at) ucsd.edu]
- Aditya Mandke [amandke (at) ucsd.edu]
- Tiffany Chu [t2chu (at) health.ucsd.edu]

## Acknowledgments

We would like to thank the authors of the original BMI dataset study for making their data available for academic research, as well as the instructors and TA's of CSE 284 at UCSD for their guidance and support throughout this project.

## License

This project is licensed under the Apache 2.0 license
