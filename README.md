

# Development of a Profile Hidden Markov Model for Kunitz-Type Protease Inhibitor Domain (Pfam: PF00014)

This repository contains a **Profile Hidden Markov Model (HMM)** designed to detect the **Kunitz-type protease inhibitor domain** (Pfam ID: PF00014) in protein sequences. Developed as part of the *Bioinformatics Master’s Program* at the **University of Bologna**, this project focuses on computational methods for sequence analysis and structural bioinformatics.
The **Kunitz domain** is an essential protein domain involved in inhibiting serine proteases and has significant roles in biological regulation and drug discovery. This project aims to develop a reliable computational tool that accurately identifies Kunitz domains through the integration of **bioinformatics techniques**, **sequence alignment**, and **model evaluation**.

---

## Overview

The Kunitz domain is a highly conserved structural unit found in many proteins, especially involved in serine protease inhibition. Detecting Kunitz domains within protein sequences is challenging in computational biology. In this work, we introduce a **Profile Hidden Markov Model (HMM)** built using experimentally validated structural data and sequence alignments. The model demonstrates outstanding performance with an **accuracy (ACC)** of 0.99995 and a **Matthews Correlation Coefficient (MCC)** of 0.9995 at an optimized **e-value threshold** of **1e−6**. The model’s robustness is further validated with **Receiver Operating Characteristic (ROC)** analysis, making it a valuable tool for the annotation of Kunitz-containing proteins.

---

## Key Terms

Kunitz domain, Hidden Markov Models, protein structure, protease inhibition, ROC analysis, model evaluation

---

## Goals

* Create a structure-based **multiple sequence alignment (MSA)** for known Kunitz-domain proteins.
* Remove redundant data using **BLAST** and **CD-HIT**.
* Develop and optimize a **Profile HMM** based on the alignment.
* Assess the model’s performance using carefully curated datasets for **true Kunitz domains** and **non-Kunitz proteins**.
* Analyze performance metrics, including **confusion matrix**, **accuracy**, **sensitivity**, and **specificity**.

---

## Prerequisites

Before running the pipeline, make sure to install the required programs within a **Conda environment**:

```bash
conda create -n kunitz_env python=3.12.7
conda activate kunitz_env
conda install -c bioconda hmmer blast biopython
conda install -c conda-forge cd-hit
```

For data visualization and plotting, the following Python libraries are utilized:

```bash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from graphviz import Digraph
```

---

## Workflow



### 1. *Extract Sequences for Kunitz Domain from UniProt*

Using the advanced search function in **UniProt**, we can retrieve sequences of proteins with the Kunitz domain using the following query:

```bash
Data Collection Resolution <= 3 AND ( Identifier = "PF00014" AND Annotation Type = "Pfam" ) AND Polymer Entity Sequence Length <= 80 AND Polymer Entity Sequence Length >= 50
```

The IDs from the results file are then used to create a FASTA file:

```bash
cat rcsb_pdb_custom_report.csv | tr -d '"' | awk -F ',' '{if (length($2)>0) {name=$2}; print name ,$3,$4,$5}' | grep PF00014 | awk '{print ">"$1"_"$3; print $2}' > pdb_kunitz_custom_reported.fasta
```

Next, **CD-HIT** is used to cluster the sequences at a **90% identity threshold**:

```bash
cd-hit -i pdb_kunitz_custom_reported.fasta -o pdb_kunitz_custom_reported.clstr -c 0.9
```

Clusters are then analyzed to remove unnecessary sequences, and the representative IDs are extracted:

```bash
awk '$5 == 1 {print $1}' pdb_kunitz.clusters.txt > pdb_kunitz_rp.ids
```

### 2. *Perform Multiple Sequence Alignment (MSA)*

For sequence alignment, we use the **PDBeFold Multi-alignment Tool**. After alignment, the sequences are formatted as follows:

```bash
awk '{if (substr($1,1,1)==">") {print "\n" toupper($1)} else {printf "%s", toupper($1)}}'> pdb_kunitz_nr.ali
```
Once the MSA is complete, we visualize the results using Jalview 2.11.4.1 to assess the structural similarities and identify conserved regions across the Kunitz domain proteins.
### 3. *Build the Profile HMM*

Using the **HMMER** software, the **Profile HMM** is constructed based on the aligned sequences:

```bash
conda activate kunitz_env
hmmbuild structural_model.hmm pdb_kunitz_nr.ali
```

### 4. *Evaluate the Model*

A **two-fold cross-validation** is performed to assess the model’s performance. We first create positive and negative sets by excluding proteins used to build the model:

```bash
cat human_kunitz.fasta human_not_kunitz.fasta > all_kunitz.fasta
makeblastdb -in all_kunitz_uniprot.fasta -dbtype prot -out all_kunitz_uniprot.fasta
blastp -query pdb_kunitz_rp.fasta -db all_kunitz_uniprot.fasta -out pdb_kunitz_nr_23.blast -outfmt 7
```

### 5. *Prepare Final Datasets*

The script *get\_seq.py* is used to filter the files and generate the final datasets:

```bash
python3 get_seq.py to_keep.ids all_kunitz_uniprot.fasta ok_kunitz.fasta
```

Randomize the positive and negative sets:

```bash
sort -R sp_negs.ids > random_sp_negs.ids
```

### 6. *Evaluate Model Performance*

Finally, the model’s performance is evaluated using **Hmmsearch**:

```bash
hmmsearch -Z 1000 --max --tblout pos_1.out structural_model.hmm pos_1.fasta
```
### 7.results
The final results are in the complete project report




## Author

**Delnia Khezragha**
Department of Pharmacy and Biotechnology, University of Bologna, Italy
Email: [delnia.khezragha@studio.unibo.it](mailto:delnia.khezragha@studio.unibo.it)

---


