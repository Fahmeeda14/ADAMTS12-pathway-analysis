setwd("C:/Users/Fahmeeda/Desktop/ADAMTS12_project/scripts")

# Read the pathway data
pathways <- read.csv(
  "../output/relevant_pathways.csv",
  check.names = FALSE
)

# Display the column names
print(names(pathways))

# Display the first six rows
print(head(pathways))

# Keep only the two columns we need
pathways <- pathways[
  ,
  c("#node", "term description")
]

# Rename those two columns
colnames(pathways) <- c(
  "gene",
  "pathway"
)

# Remove repeated gene-pathway combinations
pathways <- unique(pathways)

# Count pathways
pathway_counts <- table(pathways$pathway)

# Keep pathways shared by at least two genes
shared_counts <- pathway_counts[
  pathway_counts > 1
]

# Sort from most shared to least shared
shared_counts <- sort(
  shared_counts,
  decreasing = TRUE
)

print(shared_counts)

# To create bar plot 

# Barplot of shared pathways

barplot(
  shared_counts,
  horiz = TRUE,
  las = 1,
  cex.names = 0.6,
  col = "darkslateblue",
  main = "Pathways Shared by ADAMTS Genes",
  xlab = "Number of ADAMTS genes"
)

par(
  mar = c(5, 12, 4, 2)
)


dev.off()

# Heatmap showing which genes share each pathway
graphics.off()
library(ggplot2)

heatmap_data <- as.data.frame(gene_pathway_table)

colnames(heatmap_data) <- c(
  "gene",
  "pathway",
  "value"
)

ggplot(
  heatmap_data,
  aes(
    x = gene,
    y = pathway,
    fill = value
  )
) +
  geom_tile() +              #AI assisted section
  scale_fill_gradient(       #geom_tile() created reactangular tiles for-  
    low = "beige",           #heatmap 
    high = "darkslateblue"   #The fill colour represents whether a gene is - 
  ) +                        #associated with a pathway.
  labs(                      #formatting options to the same plot.
    title = "ADAMTS Genes and Shared Pathways",
    x = "ADAMTS gene",
    y = "Pathway"
  ) +
  theme_minimal()

# Bubble plot of functional enrichment

library(ggplot2)

enrichment <- read.csv(
  "../output/clean_enrichment_results.csv"
)

enrichment$log_FDR <- -log10(
  enrichment$FDR
)

bubble_plot <- ggplot(
  enrichment,
  aes(
    x = strength,
    y = pathway,
    size = gene_count,
    color = log_FDR
  )
) +
  geom_point() +                            #AI assisted section
  labs(                                     #geom_point()creates one bubble-
    title = "ADAMTS Functional Enrichment", #for each enriched pathway.
    x = "Enrichment strength",              #In ggplot2,+ adds layers and 
    y = "Pathway",                          #formatting options to the same 
    size = "Gene count",                    #plot.
    color = "-log10(FDR)"
  ) +
  theme_minimal()

print(bubble_plot)



