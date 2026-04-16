import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person[person.duplicated(subset=['email'], keep=False)]
    result = result['email'].drop_duplicates().to_frame()
    return result[['email']].rename(columns={'email': 'Email'})