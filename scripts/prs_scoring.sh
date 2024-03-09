# Set the paths for input and output directories
genome_path=data/bmi/ld_pruned_genotype_data/LD_pruned_PLINK/P50_round2_LD_pruned_3473
prs_dir=prs
valid_dir=valid
pvals_dir=pvals
out_dir=out

# Remove existing output directory and create a new one
rm -rf $out_dir
mkdir $out_dir

# List of filenames representing various physiological traits
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
    # Remove existing directory for the current trait and create a new one
    rm -rf ${out_dir}/${filename}
    mkdir $out_dir/${filename}
    
    # Run PLINK to calculate polygenic risk scores (PRS)
    plink \
        --bfile $genome_path \                           # Path to PLINK binary files
        --score $prs_dir/prs_${filename}_profile.txt header 2 4 7 \  # Use PRS profile file for scoring
        --q-score-range range_list ${pvals_dir}/${filename}.pvals \  # Use p-values file for Q-score range
        --extract $valid_dir/LD_pruned.valid.snp \        # Extract only valid SNPs
        --out $out_dir/${filename}/${filename}            # Output directory and filename
done
