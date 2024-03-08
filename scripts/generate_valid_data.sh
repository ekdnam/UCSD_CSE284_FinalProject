# get valid snps

dataset_path=data/bmi/ld_pruned_genotype_data/LD_pruned_PLINK/P50_round2_LD_pruned_3473.bim
output_dir=valid
output_filename=LD_pruned.valid.snp

echo "Dataset Path: $dataset_path"
echo "Output Directory: $output_dir"
echo "Output filename: $output_filename"

echo "Remove $output_dir if it exists"
rm -rf $output_dir

echo "Create $output_dir"
mkdir $output_dir

echo "Get valid snps"
awk 'NR!=1{print $2}' $dataset_path > $output_dir/$output_filename
echo "Valid snps stored at $output_dir/$output_filename"

# get range list
echo "get range list"
echo "0.000001 0 0.000001" > range_list 
echo "0.00001 0 0.00001" >> range_list 
echo "0.0001 0 0.0001" >> range_list 
echo "0.001 0 0.001" >> range_list 
echo "0.05 0 0.05" >> range_list
echo "0.1 0 0.1" >> range_list