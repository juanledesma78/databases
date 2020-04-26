
# coding: utf-8

# In[19]:


from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///c:\\path_to_directory\\kinases_v1_hk_table.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class HumanKinases(Base):
    __tablename__ = 'human_kinases'
    Entry_name = Column(String (30))
    UniProt_ID = Column(String (30),primary_key=True) 
    Primary_Protein_Name = Column (String (100))
    Alternate_Protein_Name= Column("Alternate_Protein_Name(s)",String (200)) 
    Gene_Symbol = Column(String (20))
    Alternative_Gene_Name = Column("Alternative_Gene_Name(s)", String(50)) 
    Families= Column(String (100))
    AA_sequence = Column(String (1000))
    Molecular_Mass = Column("Molecular_Mass_(Da)",Integer)
    Subcellular_Location = Column(String (500))


# The lines below are to start inteacting with the database, 
# so I assume that it would be common for the query (see below Celia) 
# as well as for the code to parse the data from the csv (Katie)
#Please check tutorial to know more

from sqlalchemy.orm import sessionmaker
Session= sessionmaker(bind=engine)
session= Session()



#This is a simple query to filter the KInases with names starting with AKT and give the info for the the name and the accession number

first_search=session.query(HumanKinases).filter(HumanKinases.Entry_name.like('AKT%'))
for x in first_search:
    print("Kinase Name",x.Entry_name,"; Uniprot ID: ",x.UniProt_ID)

