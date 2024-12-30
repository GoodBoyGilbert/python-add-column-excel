import pandas as pd

employee_data = pd.read_excel('employee_data.xlsx')


employee_data['Bonus'] = employee_data['Salary'] * .01

employee_data.to_excel('employee_data_with_bonus.xlsx', index=False)