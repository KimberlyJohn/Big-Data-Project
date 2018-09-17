#!/anaconda3/bin/python

import re
import zipfile
import pandas

from pymongo import MongoClient
from pprint import pprint
from csv import reader
from models import Patient, Gene

def main():

    # Connect to MongoClient
    client = MongoClient('localhost', 27017)

    # DB & Collections
    db = client.ad_database
    patients = db.patients
    genes = db.genes

    # Parse & Load CSV files
    parse_csv(patients, 'data/patients.csv', 'patient')
    # parse_csv(genes, 'data/entrez_ids_genesymbol.csv', 'gene')
    # parse_csv(genes, 'data/PPI.csv', 'interactors')

    # Update genes with uniprot_ids
    # insert_uniprot_ids(genes, 'data/entrez_ids_uniprot.txt')

    # Update patients with gene expression values and diagnosis
    insert_expression_values(patients, 'data/ROSMAP_RNASeq_entrez.csv.zip')


def insert_expression_values(patients, path_to_file):
    zf = zipfile.ZipFile('data/ROSMAP_RNASeq_entrez.csv.zip')
    df = pandas.read_csv(zf.open('ROSMAP_RNASeq_entrez.csv'))

    column_names = list(df.columns.values)
    lists = df.values.tolist()

    print(len(column_names))

    # for l in lists:
        # patients.update({ 'id': list[0] }, {'$set' : { 'diagnosis' : list[1], 'gene_expression' : list(zip(column_names[2:], l[2:])) }})

def insert_uniprot_ids(genes, path_to_file):
    file = open(path_to_file, 'r')
    next(file)

    for line in file:
        line = line.strip('\n').split('\t')
        entrez_id, uniprot_id = int(line[0]), line[1]

        gene = genes.find_one({ 'entrez_id' : entrez_id })

        if not gene is None:
            ids = gene['uniprot_ids']
            ids.append(uniprot_id)
            genes.update({'entrez_id' : entrez_id }, {'$set' : { 'uniprot_ids' : ids }})

    file.close()

def parse_csv(collection, path_to_file, model):
    with open(path_to_file, 'r') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader) # skips first line

        if model is 'patient':
            load_patients(collection, csv_reader)

        elif model is 'gene':
            load_genes(collection, csv_reader)

        elif model is 'interactors':
            update_genes_interactors(collection, csv_reader)

def load_patients(patients, csv_reader):
    for line in csv_reader:
        patient = Patient(line[0], int(line[1]), line[2], line[3])
        patients.insert_one(patient.get_document())

def load_genes(genes, csv_reader):
    for line in csv_reader:
        gene = Gene(int(line[0]), line[1], line[2])
        genes.insert_one(gene.get_document())

def update_genes_interactors(genes, csv_reader):
    for line in csv_reader:

        # Pull ID and find gene in DB
        entrez_id = int(line[0])
        gene = genes.find_one({ 'entrez_id' : entrez_id })

        # If gene is in DB collection, update interactsWith list
        if not gene is None:
            interactors = gene['interactsWith']
            interactors.append(int(line[1]))
            genes.update({'entrez_id' : entrez_id }, {'$set' : { 'interactsWith' : interactors }})

def document_count(patients, genes):
    print('Patients:', patients.count(), 'Genes:', genes.count())

if __name__ == "__main__":
    main()
