with open("list_of_employees", encoding='utf-8') as empl_file:
    employees = {}
    for line in empl_file:
        key, value = line.split()
        employees[key] = value
        value = int(value)
        if value < 20000:
            print(f" Employees with salary less 20000: {key}")





