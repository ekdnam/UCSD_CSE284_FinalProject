python utils/download_data.py

unzip data/bmi/ld_pruned_genotype_data/LD_pruned_PLINK.zip -d data/bmi/ld_pruned_genotype_data/

python utils/write_prs_files.py

chmod +x scripts/generate_pvals.sh
chmod +x scripts/generate_valid_data.sh
chmod +x scripts/prs_scoring.sh

./scripts/generate_pvals.sh
./scripts/generate_valid_data.sh
./scripts/prs_scoring.sh

python utils/generate_r2.py