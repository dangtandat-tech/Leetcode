import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employee, employee, left_on = 'managerId', right_on = 'id', how='left')
    result = result[result['salary_x'] > result['salary_y']]
    result = result[['name_x']].rename(columns = {'name_x': 'Employee'})
    return result