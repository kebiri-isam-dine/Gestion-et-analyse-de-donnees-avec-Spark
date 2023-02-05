# -*- coding: UTF-8 -*-
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

fichier = "../data/FANTOIR0117"

schema = avro.schema.parse(open("fantoir_lieudit.avsc", "rb").read())
f = open(fichier, "r")

# Enregistrement initial
f.readline()

writer = DataFileWriter(open("lieuxdits.avro", "wb"), DatumWriter(), schema)

for ligne in f: 
    if len(ligne[:10].rstrip()) == 10:
        type = "lieu-dit"
        commune = ligne[0:6].rstrip()
        identifiant = ligne[6:10].rstrip()
        codeNature = ligne[11:15].rstrip()
        libelle = ligne[15:41].rstrip()
        caractere = ligne[48:49]
        typeVoie = ligne[108:109]

        d = {"commune": commune, "identifiant": identifiant, "nature": codeNature, "libelle": libelle, "caractere": caractere, "voie": typeVoie}
        writer.append(d)
    
f.close()
writer.close()
