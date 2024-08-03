# Paper Readings and References

This note contains various paper's read, references for citations regarding protein analysis we used for NCC or general. This may inclue links, some notes and important points for a paper, etc.

## 1. Inference of Protein Function from Protein Structure

---

pdf/doc link: https://www.cell.com/action/showPdf?pii=S0969-2126%2804%2900389-2
Pubmed: https://pubmed.ncbi.nlm.nih.gov/15642267/
Other links:

1. https://www.cell.com/structure/fulltext/S0969-2126(04)00389-2?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0969212604003892%3Fshowall%3Dtrue

---

### Abstract

Structural genomics has brought us three-dimensional structures of proteins with unknown functions. To shed light on such structures, we have developed ProKnow (http://www.doe-mbi.ucla.edu/Services/ProKnow/), which annotates proteins with Gene Ontology functional terms. The method extracts features from the protein such as 3D fold, sequence, motif, and functional linkages and relates them to function via the ProKnow knowledgebase of features, which links features to annotated functions via annotation profiles. Bayes' theorem is used to compute weights of the functions assigned, using likelihoods based on the extracted features. The description level of the assigned function is quantified by the ontology depth (from 1 = general to 9 = specific). Jackknife tests show approximately 89% correct assignments at ontology depth 1 and 40% at depth 9, with 93% coverage of 1507 distinct folded proteins. Overall, about 70% of the assignments were inferred correctly. This level of performance suggests that ProKnow is a useful resource in functional assessments of novel proteins.

### Notes

- Knowing sequence and structure does not guarantee knowing protein function, especially in cases where there is no history of experimental characterization.
- in silico methods capable of function annotation of proteins must be extended.

---

#### Existing models and methods

- A protein with a high degree of sequence similarity to a family of well-characterized proteins can be detected by BLAST.
- With lower sequence similarity, more subtle methods such as “profiles” (where patterns obvious from multiple sequence alignment are evident) or hidden Markov models (HMM) are required.
- Feature Extractors: DALI/DASEY, RIGOR, PSI-BLAST, PROSITE, DIP

---

- assumption that similar sequences have descended from a common ancestor and share similar function, with limitations mentioned in paper.
- ProKnow has each protein feature is associated with all potential functions.
- FlowChart(DAG): Feature Extractor => Protein Features -> Clues each feature gives -> ProKnow Knowledgebase => Functions mapped to protein features by Annotation Profiles -> Bayes' Theorem => Function Weights <=> Function Assignment
- GO(Gene Ontology) can be Biological Process or Molecular Function. GO desciption level bw 1(general) to 9(specific).
- Results have been properly described which can be read from the paper since it is a bit lengthy to write here.
- An important aspect of interpretation of any ProKnow assignment is an understanding of the weights on which it was inferred. A high confidence assignment is one that has BW R 0.4, CC > 4, and ER < 5, the order of their importance being BW > CC > ER.

### Conclusion

- The method integrates various programs, such as PSI-BLAST, PROSITE, DALI, and RIGOR, to extract similarity of the query protein to protein features in the ProKnow knowledgebase.
- These features include sequence, fold, motifs, and functional linkages. The annotation profile of features stored in the precompiled knowledgebase is used to map features to functions.
- The likelihood of the function is derived using Bayesian scoring by updating weights obtained from individual protein features. In this scheme, functions linked to a maximum number of protein features are used for scoring.
- The final output is a list of functions and their Bayesian weights. The evaluation of our method gave a specificity of w0.89 at ontology depth 1 and 0.4 at depth 9; the coverage was 93%. Around 70% of the annotations were assigned correctly.
- The architecture of our method also allows us to predict function from sequence alone.
- An application of ProKnow to the TB genome shows that ProKnow is able to assign around 50% of genes in the genome with high confidence.
- This was also tested the method on enzyme-nonenzyme homologous partners with distinct function, where the method detected the majority of functional dissimilarities.

## 2. Predicting protein function from sequence and structural data

---

doi link: https://doi.org/10.1016/j.sbi.2005.04.003
sciencedirect link: https://www.sciencedirect.com/science/article/pii/S0959440X05000825?via%3Dihub
pubmed link: https://pubmed.ncbi.nlm.nih.gov/15963890/

---

### Abstract

When a protein's function cannot be experimentally determined, it can often be inferred from sequence similarity. Should this process fail, analysis of the protein structure can provide functional clues or confirm tentative functional assignments inferred from the sequence. Many structure-based approaches exist (e.g. fold similarity, three-dimensional templates), but as no single method can be expected to be successful in all cases, a more prudent approach involves combining multiple methods. Several automated servers that integrate evidence from multiple sources have been released this year and particular improvements have been seen with methods utilizing the Gene Ontology functional annotation schema.

### Notes

- Basically is based upon structure based predictions of protein function.
- Structure can provide clues to function in many cases, even if powerful sequence methods have failed to provide a conclusive functional assignment.
- A sensible strategy to subject the target to a battery of different prediction methods. Web servers such as ProFunc and ProKnow are being developed to do just that.
- This paper mainly talks about web servers, pre existing methods and nothing add new on his own. It is like a discussion on multiple methods.

## 3. Protein function prediction as approximate semantic entailment

---

nature: https://www.nature.com/articles/s42256-024-00795-w
pdf/doc: https://www.nature.com/articles/s42256-024-00795-w.pdf
doi: https://doi.org/10.1038/s42256-024-00795-w

---

### Abstract

The Gene Ontology (GO) is a formal, axiomatic theory with over 100,000 axioms that describe the molecular functions, biological processes and cellular locations of proteins in three subontologies. Predicting the functions of proteins using the GO requires both learning and reasoning capabilities in order to maintain consistency and exploit the background knowledge in the GO. Many methods have been developed to automatically predict protein functions, but effectively exploiting all the axioms in the
GO for knowledge-enhanced learning has remained a challenge. We have developed DeepGO-SE, a method that predicts GO functions from protein sequences using a pretrained large language model. DeepGO-SE generates multiple approximate models of GO, and a neural network predicts the truth values of statements about protein functions in these approximate models. We aggregate the truth values over multiple models so that DeepGO-SE approximates semantic entailment when predicting protein functions.
We show, using several benchmarks, that the approach effectively exploits background knowledge in the GO and improves protein function prediction compared to state-of-the-art methods.

## 4. Structure-based protein function prediction using graph convolutional networks

---

nature link: https://www.nature.com/articles/s41467-021-23303-9
pdf/doc: https://www.nature.com/articles/s41467-021-23303-9.pdf
doi: https://doi.org/10.1038/s41467-021-23303-9

---

### Abstract

The rapid increase in the number of proteins in sequence databases and the diversity of their functions challenge computational approaches for automated function prediction. Here, we introduce DeepFRI, a Graph Convolutional Network for predicting protein functions by leveraging sequence features extracted from a protein language model and protein structures. It outperforms current leading methods and sequence-based Convolutional Neural Networks and scales to the size of current sequence repositories. Augmenting the training set of experimental structures with homology models allows us to significantly expand the number of predictable functions. DeepFRI has significant de-noising capability, with only a minor drop in performance when experimental structures are replaced by protein models. Class activation mapping allows function predictions at an unprecedented resolution, allowing site-specific annotations at the residue-level in an automated manner. We show the utility and high performance of our method by annotating structures from the PDB and SWISS-MODEL, making several new confident function predictions. DeepFRI is available as a webserver at https://beta.deepfri.flatironinstitute.org/.

## Other References for ML and Protein Analysis

- Using A Neural Network and Spatial Clustering to Predict the Location of Active Sites in Enzymes

---

scienedirect link: https://www.sciencedirect.com/science/article/pii/S0022283603005151
doi link: https://doi.org/10.1016/S0022-2836(03)00515-1

---
