import pandas as pd

# Read the STRING interaction file
network = pd.read_csv(
    "../input/ADAMTS_STRING_interaction.tsv",
    sep="\t"
)

# Rename important coloumns

network = network.rename(
    columns={
        "#node1": "gene1",
        "node2": "gene2",
        "combined_score": "interaction_score"
    }
)

# Keep only selected coloumns
network = network[
    ["gene1", "gene2", "interaction_score"]
]

# Create a standard order for each gene pair

network["first_gene"] = network[
    ["gene1", "gene2"]
].min(axis=1)

network["second_gene"] = network[
    ["gene1", "gene2"]
].max(axis=1)

# Remove duplicate reciprocal interactions
network = network.drop_duplicates(
    subset=["first_gene", "second_gene"]
)

# Remove temporary columns
network = network.drop(
    columns=["first_gene", "second_gene"]
)

# Save the cleaned network
network.to_csv(
    "../output/clean_network.csv",
    index=False
)

# Print the result
print("Clean interaction network:")
print(network)