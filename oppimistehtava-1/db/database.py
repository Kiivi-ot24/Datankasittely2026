from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User
from configuration import DATABASE_URL

# Luodaan tietokantamoottori ja sessionmaker. Tietokantayhteyden hallinta erotettu omaan moduuliin.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# save_users funktio, joka tallentaa käyttäjät tietokantaan
def save_users(users):
    with SessionLocal.begin() as session:
        for user_data in users:
            session.merge(User(**user_data))