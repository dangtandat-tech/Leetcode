import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person.groupby('email').filter(lambda x: len(x) > 1)
    result = result['email'].drop_duplicates().to_frame()
    return result[['email']].rename(columns={'email': 'Email'})