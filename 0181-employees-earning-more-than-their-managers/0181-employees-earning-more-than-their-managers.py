import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(
        employee,
        left_on = 'managerId',
        right_on = 'id',
        suffixes = ('_em', '_mg')
    )
    result = result[result['salary_em'] > result['salary_mg']]
    result = result[['name_em']].rename(columns = {'name_em': 'Employee'})
    return result