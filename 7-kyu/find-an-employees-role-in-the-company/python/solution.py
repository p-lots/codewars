def find_employees_role(name):
    try:
        first, last = name.split(' ')
        for employee in employees:
            if employee['first_name'] == first and employee['last_name'] == last:
                return employee['role']
        return 'Does not work here!'
    except:
        return 'Does not work here!'