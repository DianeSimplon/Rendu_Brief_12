import psycopg2
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, Computed

#Connection à ma base de donnees en passant par python
conn = psycopg2.connect("dbname=imo_import user=diane host=localhost port=5432 password=password");
conn.cursor()

#C'est c'est des utilisateur qui se connecte: est ça marche
engine = create_engine('postgresql+psycopg2://imp_import:diane@localhost/imo_import')
print(engine)
