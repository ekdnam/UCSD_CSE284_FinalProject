## Option 2: Generate PRS for BMI and test on real data from open field studies

* PRS on rat BMI data, test on open field study data, validate on social interaction data. All datasets are in rats to avoid population portability issues between human datasets.

## BMI and Psychiatric Disorders

Recent research in humans suggest that there may be an association between increased BMI and psychiatric genetic markers.

* Body mass index and psychiatric disorders: a Mendelian randomization study (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5013405/)
* The Impact of BMI on Mental Health: Further Evidence from Genetic Markers (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9062912/)
* Psychiatric disorders and obesity: A review of association studies (2017) (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5525483/)
* https://www.nature.com/articles/s44220-023-00158-1 (2024) (https://www.nature.com/articles/s44220-023-00158-1)
* Shared genetics between classes of obesity and psychiatric disorders: A large-scale genome-wide cross-trait analysis (https://www.sciencedirect.com/science/article/abs/pii/S0022399922003178)

## Interpretation

We will examine the top SNPs that pass p-value and power thresholds. We will look on the Genome Browser for the SNP locations and upstream / downstream genes. We will also do primary literature evaluation for published data related to our SNPs of interest. We expect that we will find a few SNPs that implicate an association between high BMI and psychiatric behaviors.

## Datasets

The test datasets are subsetted from "Genome-Wide Association Study on Three Behaviors Tested in an Open Field in Heterogeneous Stock Rats Identifies Multiple Loci Implicated in Psychiatric Disorders." Two separate studies make up this dataset.

The first study is the Novel Object Interaction Test. A 3D printed cylindrical rat cage with 24 rods, the novel object, was placed in the middle of the field. Rats were given 20 minutes to find and explore the object. Control rats preferentially explore the novel object. Decreased interest or avoidance of the novel object can underly psychiatric disorder behaviors.

The second study is the Social Interaction Test. A subject rat and a stimulus rat are introduced to each other. Each pair of rats had never been housed together, and therefore are unfamiliar with each other before the test. Because rats are social animals, it is expected that a control subject rat will preferentially spend more time interacting with the stimulus rat. In previous studies with rats with autism spectrum behaviors or social interaction disorders, subject rats either spend an equal time alone versus the stimulus rat, or spend preferential time alone.

## Issues

The validation and test datasets are subsetted from "Genome-Wide Association Study on Three Behaviors Tested in an Open Field in Heterogeneous Stock Rats Identifies Multiple Loci Implicated in Psychiatric Disorders."  Heterogeneous stock rats are laboratory rats that have been cross-bred for heterogenicity. They therefore have more variability than the traditional standard inbred rats. Howver, these rats did start from standard laboratory rat lines and eventually become used to human handlers, so they are not equivalent to truely wild rats. Due to their starting genetic origin, there may be some confounding in our study due to cryptic relatedness between the rats which may explain our inflated p-values in the QQ plot.