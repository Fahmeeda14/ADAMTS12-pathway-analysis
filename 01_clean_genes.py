import pandas as pd

#Read CSV File
genes = pd.read_csv(
    "../input/ADAMTS_ocular_genes.csv"
)

# Select Gene-Name coloumn
gene_names = genes["ADAMTS Gene Members"]

#Remove blank cells
gene_names = gene_names.dropna()

#Convert gene names to text
gene_names = gene_names.astype(str)

# Remove extra spaces
gene_names = gene_names.str.strip()

#Remove duplicate gene names
gene_names = gene_names.drop_duplicates()

#Add ADAMTS12 if it is missing
if "ADAMTS12" not in gene_names.values:
    gene_names = pd.concat(
        [gene_names, pd.Series(["ADAMTS12"])],
        ignore_index=True
    ) # concat joins existing gene lists with a new one item list. # ignore_index=True gives the rows clean numbers starting from zero. 

#Saving the cleaned list
gene_names.to_csv(
    "../output/clean_gene_list.csv",
    index=False,
    header=["gene"]
)

# Print the final list
print("Clean gene list:")
print(gene_names.tolist())

