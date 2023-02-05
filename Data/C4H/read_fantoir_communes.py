# -*- coding: UTF-8 -*-
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

fichier = "../data/FANTOIR0117"

schema = avro.schema.parse(open("fantoir_commune.avsc", "rb").read())
f = open(fichier, "r")

# Enregistrement initial
f.readline()

writer = DataFileWriter(open("communes.avro", "wb"), DatumWriter(), schema)
for ligne in f: 
    #print (len(ligne))
    if len(ligne[:10].rstrip()) == 3:
        type = "dept"
    elif len(ligne[:10].rstrip()) == 6:
        type = "commune"
        nom = ligne[11:41].rstrip()
        typeCommune = ligne[42:43]
        population = int(ligne[52:59])
    elif len(ligne[:10].rstrip()) == 10:
        type = "lieu-dit"
            
    if type == "commune":
        print (ligne[:6], type, nom, typeCommune, population)
        d = {"code": ligne[:6], "nom": nom, "type_commune": typeCommune, "population": population}
        writer.append(d)
    
f.close()
writer.close()
