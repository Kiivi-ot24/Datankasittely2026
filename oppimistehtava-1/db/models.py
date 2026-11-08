from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Päätin sisällyttää kaikki API:sta tulevat kentät tietokantaan
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)
    latitude = Column(Float) # latitude ja longitude määritelty float:ksi stringin sijaan, siltä varalta että jos niitä halutaan käyttää myöhemmin laskentaan
    longitude = Column(Float)

    phone = Column(String)
    website = Column(String)

    company_name = Column(String)
    company_catch_phrase = Column(String)
    company_bs = Column(String)
