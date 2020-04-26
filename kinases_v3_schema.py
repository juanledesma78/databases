
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
engine = create_engine('sqlite:///c:\\sqlite\\kinases_v3_schema.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
class HumanKinases(Base):
    __tablename__ = 'human_kinases'
    Entry_name = Column(String (15))
    UniProt_ID = Column(String (10),primary_key=True) 
    Primary_Protein_Name = Column (String (100))
    Alternative_Protein_Name= Column("Alternate_Protein_Name(s)",String (350)) 
    Gene_Symbol = Column(String (15))
    Alternative_Gene_Name = Column("Alternative_Gene_Name(s)", String(60)) 
    Families= Column(String (175))
    AA_seq = Column(String (34400))
    Molecular_Mass = Column("Molecular_Mass_(Da)",String (10))
    Subcellular_Location = Column(String (350))
    kinases_phosphosites = relationship("KinasesPhosphosites", backref="human_kinases")
    inhib_kin = relationship("InhibKin", backref="human_kinases")
    
class Phosphosites(Base):
    __tablename__ = 'phosphosites'
    GENE = Column(String(20))
    PROTEIN = Column(String(20))
    ACC_ID = Column(String(19))
    HU_CHR_LOC = Column(String(26))
    MOD_RSD = Column(String(6))
    SITE_GRP_ID = Column(String(10))
    MW_kD = Column(Integer)
    DOMAIN = Column(String(30)) 
    SITE_7_AA = Column("SITE_+/-7_AA", String(15))
    LT_LIT = Column(Integer)
    MS_LIT = Column(Integer)
    MS_CST = Column(Integer)
    CST_CAT = Column("CST_CAT#", String(141))
    SOURCE = Column (String(66))
    SEQUENCE = Column(String (8797)) 
    PMID = Column(String (8))
    PHOS_ID5 = Column(String(24), primary_key=True)
    PHOS_ID = Column(String(31))
    PHOS_ID2 = Column(String(26))
    PHOS_ID3 = Column(String(32))
    PHOS_ID4 = Column(String(25))
    ISOFORM = Column(Integer)
    ID_PH = Column(String(9))  
    kinases_phosphosites = relationship("KinasesPhosphosites", backref="phosphosites")
    kinases_phosphosites = relationship("PhosphositesDiseases", backref="phosphosites")

class Inhibitors(Base):
    __tablename__ = 'inhibitors'
    Inhibitor = Column (String (134), primary_key=True)
    Ki_nM = Column (String(7))
    IC50_nM = Column (String(10))
    Kd_nM = Column (String(7))
    EC50_nM = Column (String(11))
    POC = Column (String(5))
    Source = Column (String(9))
    IMG_URL = Column (String (79))
    ID_IN = Column (String (9))
    inhib_kin = relationship("InhibKin", backref="inhibitors")
    #tablename_to_link = relationship("Class_of_tablename_to_link",backref="this_tablename" )


class KinasesPhosphosites(Base):
    __tablename__ = 'kinases_phosphosites'
    GENE = Column(String(13))
    KIN_ACC_ID = Column (String(9))
    SUB_ACC_ID = Column (String(17))
    IN_VIVO_RXN = Column(String(1))
    IN_VITRO_RXN = Column(String(1))
    CST_CAT = Column("CST_CAT#", String(141))
    SOURCE = Column (String(64))
    SEQUENCE = Column (String (8797))
    PMID = Column (String(8))
    PHOS_ID5 = Column(String(23), ForeignKey('phosphosites.PHOS_ID5'))
    PHOS_ID = Column(String(31))
    PHOS_ID2 = Column(String(23))
    PHOS_ID3 = Column(String(29))
    PHOS_ID4 = Column(String(25))
    KIN_ACC_ID_2 = Column (String (10),ForeignKey('human_kinases.UniProt_ID'))
    ID_KS = Column(String(9), primary_key=True)


class PhosphositesDiseases(Base):
    __tablename__ = 'phosphosites_diseases'
    DISEASE = Column(String(92))
    ALTERATION = Column(String(32)) 
    ACC_ID = Column(String(16))
    PMIDs = Column(String(8))
    LT_LIT = Column(Integer)
    MS_LIT = Column(Integer)
    MS_CST = Column(Integer)
    CST_CAT = Column("CST_CAT#", String(141))
    NOTES = Column(String(314))
    PHOS_ID = Column(String(22), ForeignKey('phosphosites.PHOS_ID5'))  # duplicates
    ID_PD = Column(String(9), primary_key=True)

class InhibKin(Base):
    __tablename__ = 'inhib_kin'
    Kinase = Column(String(8)) 
    Inhibitor = Column (String (134), ForeignKey('inhibitors.Inhibitor'))
    UniProt_ID = Column (String(6), ForeignKey('human_kinases.UniProt_ID'))
    ID_KI = Column (String (9), primary_key=True)

Base.metadata.create_all(engine)

