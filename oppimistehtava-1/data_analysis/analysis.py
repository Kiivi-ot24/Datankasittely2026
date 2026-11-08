import pandas as pd

def analyze_users(users):

    df = pd.DataFrame(users)

    print("Data shape:", df.shape) # Printataan daraframen shape = rivien ja sarakkeiden määrä
    print("\nFirst two records:")
    print(df.head(2).to_string(index=False)) # head(2) = printataan kaksi ensimmäistä riviä
    print("\nLast two records:")
    print(df.tail(2).to_string(index=False)) # tail(2) = printataan kaksi viimeistä riviä

    return df 