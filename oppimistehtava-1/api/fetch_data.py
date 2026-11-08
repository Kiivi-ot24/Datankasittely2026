import requests
from configuration import API_URL

def fetch_users():
    response = requests.get(API_URL) # GET-pyyntö API_URL
    response.raise_for_status() # Tarkastetaan että pyyntö onnistui
    api_users = response.json() # Muutetaan JSON-vastaus Pythonille sopivaksi


    # Sisäkköiset sarakkeet (esim. address ja company) puretaan yksittäisiksi sarakkeiksi
    return [
        {
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "street": user["address"]["street"],
            "suite": user["address"]["suite"],
            "city": user["address"]["city"],
            "zipcode": user["address"]["zipcode"],
            "latitude": user["address"]["geo"]["lat"],
            "longitude": user["address"]["geo"]["lng"],
            "phone": user["phone"],
            "website": user["website"],
            "company_name": user["company"]["name"],
            "company_catch_phrase": user["company"]["catchPhrase"],
            "company_bs": user["company"]["bs"],
        }
        for user in api_users
    ]

# Siltä varalta että halutaan testata API-hakua erikseen
if __name__ == "__main__": 
    fetch_users()
    