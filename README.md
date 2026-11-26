# ADAMTS12-pathway-analysis
Class project : Python and R analysis of ADAMTS12-related genes, pathways, enrichment, and interaction partners.

## Aim
To investigate the biological context of ADAMTS12 by analyzing ocular ADAMTS genes, shared pathways, functional enrichment, and other proteins associated with ADAMTS12.

## Code
Python was used to:
- clean the gene list
- clean the STRING interaction data
- filter relevant pathways
- identify shared pathways
- prepare enrichment results
- identify non-ADAMTS12 interaction partners

R was used to create:
- a shared-pathway bar plot
- a gene–pathway heatmap
- a functional-enrichment bubble plot

## Input files
The analysis used the following input files:
1. ADAMTS_ocular_genes.csv — literature-based ocular ADAMTS gene list
2. ADAMTS_STRING_interaction.tsv — STRING interaction data
3. ADAMTS_STRING_functional_annotations.tsv — STRING functional annotations
4. enrichment.Process.tsv — biological-process enrichment results
5. enrichment.Function.tsv — molecular-function enrichment results
6. enrichment.RCTM.tsv — Reactome enrichment results
7. ADAMTS12_first_shell_medium.tsv — ADAMTS12 first-shell interaction data

## Main scripts
- 01_clean_genes.py — cleans the ocular ADAMTS gene list
- 02_clean_network.py — removes reciprocal interaction duplicates
- 03_filter_pathways.py — filters relevant pathway terms
- 04_shared_pathways.py — identifies shared pathways
- 05_check_enrichment.py — checks the enrichment file
- 06_clean_enrichment.py — prepares enrichment results
- 07_check_ADAMTS12_partners.py — checks ADAMTS12 partners
- 08_select_external_partners.py — selects non-ADAMTS12 partners
- 09_generate_figures.R — generates the figures

## Software
- Python
- pandas
- R
- ggplot2
- STRING database

## Use of AI
AI was used as a learning and support tool during this project. It helped explain some Python and R code and syntax, clarify error messages and suggest code improvements.
