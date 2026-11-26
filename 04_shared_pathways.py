import pandas as pd

# Read the filtered pathway file
pathways = pd.read_csv(
    "../output/relevant_pathways.csv"
)

# Rename the gene column
pathways = pathways.rename(
    columns={"#node": "gene"}
)

# Count how many different genes are linked to each pathway
pathway_counts = (
    pathways.groupby("term description")["gene"]
    .nunique()
)

# Keep pathways shared by at least two genes
shared_counts = pathway_counts[
    pathway_counts > 1
]

# Sort from most shared to least shared
shared_counts = shared_counts.sort_values(
    ascending=False
)

# Save the pathway counts
shared_counts.to_csv(
    "../output/shared_pathways.csv"
)

# Keep the detailed rows for the shared pathways
shared_terms = shared_counts.index
shared_details = pathways[
    pathways["term description"].isin(shared_terms)
]

# Sort the detailed table
shared_details = shared_details.sort_values(
    "term description"
)

# Save the detailed result
shared_details.to_csv(
    "../output/shared_pathway_details.csv",
    index=False
)

# Display the results
print("Shared pathways:")
print(shared_counts)
