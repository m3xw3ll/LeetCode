import pandas as pd


def select_first_rows(employees):
    return employees.head(3)


if __name__ == '__main__':
    data = [[3, 'Bob', 'Operations', 48675],
            [90, 'Alice', 'Sales', 11096],
            [9, 'Tatiana', 'Engineering', 33805],
            [60, 'Annabelle', 'InformationTechnology', 37678],
            [49, 'Jonathan', 'HumanResources', 23793],
            [43, 'Khaled', 'Administration', 40454],
            ]
    employee = pd.DataFrame(data, columns=['employee_id', 'name', 'department', 'salary'])
    print(select_first_rows(employee))