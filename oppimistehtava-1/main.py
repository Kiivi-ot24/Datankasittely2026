from api.fetch_data import fetch_users
from db.database import save_users
from data_analysis.analysis import analyze_users
from data_protection.masking import mask

# Suoritetaan kaikki vaiheet peräkkäin
def main():
    print("Step 1: Fetch API data...")
    users = fetch_users()

    print("\nStep 2: Save data to database...")
    save_users(users)

    print("\nStep 3: Data masking...")
    masked_users = mask(users)

    print("\nStep 4: Pandas data analysis...")
    analyze_users(masked_users)


if __name__ == "__main__":
    main()