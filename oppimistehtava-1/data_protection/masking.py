import pandas as pd


def mask(Users):
    df = pd.DataFrame(Users)

    df["name_initial"] = df["name"].str[0]  # Säilytetään nimestä ensimmäinen kirjain name_initial sarakkeeseen ja tiputetaan alkuperäinen name sarake 
    df = df.drop(columns=["name"])

    df["phone"] = df["phone"].str.replace(r".(?=.{2})", "*", regex=True)    # Maskataan puhelinnumeron kaikki merkit paitsi kaksi viimeistä tähdellä

    return df.to_dict(orient="records") # Palautetaan DataFrame takaisin dictionary muodossa
