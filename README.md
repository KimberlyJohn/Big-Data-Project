# Big Data Project Assignment: 

Developed a knowlegde base, which allows users to mine genomic data of Alzheimer's Disease Patients. 
Given Raw Data files: 
• Gene interaction (entrez id)
• Expression profile (entrez id)
• Entrez id uniprot mapping (entrez id -> uniprot id)
• Uniprot KB and Schema (uniprot id)
• Patient information

The knowledge base answers the following questions 
1) Given a gene, find all of its n-order interacting
genes
2) Given a gene, find mean and std of gene
expression values for AD/MCI/NCI, respectively
3) Given a gene, find all other information associated
with this gene.
4) Given a patient id, find all patient information (age,
gender, education etc.)


MongoDB (can be used for all queries N-order, statistical data, gene information, and patient data) 

MySQL ( used only for patient info ) being that the patient data is queried by ID 
it makes sense to use ID as a key.

Allows users to mine genomic data of Alzheimer's Disease from the provided patient and gene spreadsheets. 



Included in this repository 

A python command-line client interface for database creation and quert

Use of non-relational and relational stores. MySQL & MongoDB 


How to Run: 
python driver_query.py on command line
