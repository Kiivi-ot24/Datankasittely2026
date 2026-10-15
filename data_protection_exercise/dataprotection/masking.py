import pandas as pd


def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    df = pd.DataFrame(people)

    parts = df["email"].str.split("@", n=1, expand=True)
    local_part = parts[0]
    domain_part = parts[1]

    masked_local = local_part.replace(r"^[^@]+(?=@)", "*****", regex=True)
    
    df["email"] = masked_local + "@" + domain_part
    
    df["phone"] = df["phone"].map(lambda phone: "*" * (len(phone) -2) + phone[-2:])

    return df.to_dict(orient="records")