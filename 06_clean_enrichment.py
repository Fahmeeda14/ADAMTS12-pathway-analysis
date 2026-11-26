import pandas as pd

# Read the Biological Process enrichment file
enrichment = pd.read_csv(
    "../input/enrichment.Process.tsv",
    sep="\t"
)

# Keep the important columns
clean = enrichment[
    [
        "term description",
        "observed gene count",
        "false discovery rate",
        "strength"
    ]
]

# Rename columns for easier use in R
clean = clean.rename(
    columns={
        "term description": "pathway",
        "observed gene count": "gene_count",
        "false discovery rate": "FDR"
    }
)

# Keep statistically enriched pathways
clean = clean[
    clean["FDR"] < 0.05
]

# Sort by strongest statistical significance
clean = clean.sort_values(
    "FDR"
)

# Save the cleaned enrichment results
clean.to_csv(
    "../output/clean_enrichment_results.csv",
    index=False
)

print("Clean enrichment results:")
print(clean)