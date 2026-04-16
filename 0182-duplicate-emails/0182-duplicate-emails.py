import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = person[person['email'].duplicated()]['email'].unique()
    return pd.DataFrame({'Email': res})