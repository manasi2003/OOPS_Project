db = {101:{'name':'manasi','city':'pune', 'passing_year': 2025, 
'Percentage':88,'course':'python','fee':20000}}

print(f'{" " *45}The Kiran Academy')
print("-"*100)
while True:
    print("""
    1.Add Student Details
    2.Display Student Details
    3.Update Student Details
    4.Delete Student Details
    5.Search Student Details
    6.Filter Student Details
    """)
    ch = int(input("Enter your choice: "))
    if ch==1:
        reg = eval(input("Enter registration number: "))
        name = (input("Enter name: "))
        city = (input("Enter city name: "))
        p_y = eval(input("Enter Passing Year: "))
        per = eval(input("Enter Percentage: "))
        course = (input("Enter course: "))
        fee = eval(input("Enter fee: "))
        
        db[reg] = {'name': name, 'city': city, "passing_year": p_y, 'Percentage':per,
            'course': course, 'fee':fee}
        print("Successfully added records")
        pass
    elif ch==2:
        print('-' * 116)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration Number', 'Name', 
        'City', 'Passing year', 'Percentage', 'Course', 'Fee'))
        print('-' * 116)
        for reg in db:
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],
                db[reg]['city'],db[reg]['passing_year'],db[reg]['Percentage'],db[reg]['course'],
                db[reg]['fee']))
                print('-' * 116)
        pass
    elif ch==3:
        reg = int(input("Enter registration number: "))
        print("""
              1.Name
              2.City
              3.Passing Year
              4.Percentage
              5.Course
              6.Fee  
            """)
        ch = int(input("Enter your choice: "))
        if ch==1:
            un = input("Enter name: ")
            db[reg]['name'] = un
            print("Updated Successfully")
            pass
        elif ch == 2:
             uc = input("Enter city: ")
             db[reg]['city'] = uc
             print("Updated Successfully")
             pass
        elif ch == 3:
             up = input("Enter passing year: ")
             db[reg]['passing_year'] = up
             print("Updated Successfully")
             pass
        elif ch == 4:
            uper = input("Enter percentage: ")
            db[reg]['percentage'] = uper
            print("Updated Successfully")
            pass
        elif ch == 5:
            uco = input("Enter course: ")
            db[reg]['course'] = uco
            print("Updated Successfully")
            pass
        elif ch == 6:
            uf = input("Enter fee: ")
            db[reg]['fee'] = uf
            print("Updated Successfully")
            pass
        else:
            print("Invalid Input")
        pass
    elif ch==4:
        reg = int(input("Enter the registration number to delete: "))
        if reg in db:
            del db[reg]
            print(f"Student record with Registration Number {reg} has been deleted.")
        else:
            print("Registration number not found.")
        pass
    elif ch==5:
        reg = int(input("Enter the registration number to search: "))
        if reg in db:
            print('-' * 116)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(
            'Registration Number', 'Name', 'City', 'Passing year', 'Percentage', 'Course', 'Fee'))
            print('-' * 116)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(
            reg, db[reg]['name'], db[reg]['city'], db[reg]['passing_year'],
            db[reg]['Percentage'], db[reg]['course'], db[reg]['fee']))
            print('-' * 116)
        else:
            print("Registration number not found.")
        pass
    elif ch == 6:
        print("""
        1. Filter by City
        2. Filter by Percentage
        3. Filter by Course
    """)
        filter_choice = int(input("Enter your filter choice: "))
        if filter_choice == 1:
            city = input("Enter the city to filter by: ")
            filtered_students = {reg: details for reg, details in db.items() if details['city'].lower() == city.lower()}
        elif filter_choice == 2:
            percentage = float(input("Enter the minimum percentage to filter by: "))
            filtered_students = {reg: details for reg, details in db.items() if details['Percentage'] >= percentage}
        elif filter_choice == 3:
            course = input("Enter the course to filter by: ")
            filtered_students = {reg: details for reg, details in db.items() if details['course'].lower() == course.lower()}
        else:
            print("Invalid filter choice.")
        continue

        if filtered_students:
            print('-' * 116)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(
            'Registration Number', 'Name', 'City', 'Passing year', 'Percentage', 'Course', 'Fee'))
            print('-' * 116)
            for reg, details in filtered_students.items():
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(
                reg, details['name'], details['city'], details['passing_year'],
                details['Percentage'], details['course'], details['fee']))
            print('-' * 116)
        else:
            print("No records match the filter criteria.")
        pass
        
    else:
        print("Wrong Input")
    c = input("Do you want to continue(y/n): ")
    if c == 'n':
        break