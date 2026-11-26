import pandas as pd

# Read the STRING functional-annotation file

annotations = pd.read_csv(
    "../input/ADAMTS_STRING_functional_annotations.tsv",
    sep="\t"
)

# Terms related to ocular and extracellular-matrix biology
keywords = [
    "extracellular",
    "collagen",
    "adhesion",
    "eye",
    "visual",
    "TGF",
    "proteolysis"
]

# Join the keywords using OR
pattern = "|".join(keywords)

# Keep rows containing at least one keyword
relevant_pathways = annotations[
    annotations["term description"]
    .str.contains(pattern, case=False, na=False)
]

# Save the filtered pathways
relevant_pathways.to_csv(
    "../output/relevant_pathways.csv",
    index=False
)

# Display a summary
print("Relevant pathways saved.")
print("Number of rows:", len(relevant_pathways))
print(relevant_pathways.head())