cars = [{'vin': '123abc', 'brand': 'Toyota', 'model': 'Innova', 'year': '2011'},
        {'vin': '124abc', 'brand': 'Honda', 'model': 'CRV', 'year': '2018'}]

# Create data func
def Create_Data():
    create = True
    while create != '2':
        print('1. Add data')
        print('2. Back to Homepage')
        create = input('Choose Options: ')
        if create == "1":
            vin = input('Input VIN: ')
            for i in cars:
                if i['vin'] == vin:
                    print('Data already exists')
                    break
            else:
                brand = input('Input Brand: ')
                model = input('Input Model: ')
                year = input('Input Year: ')
                save = True
                while save:
                    save_as = input('Save data? (yes/no): ')
                    if save_as == 'yes':
                        data = {'vin': vin, 'brand': brand, 'model': model, 'year': year}
                        cars.append(data)
                        print('Data saved')
                        save = False
                    elif save_as == 'no':
                        print('Data has not been saved')
                        save = False
        elif create == "2":
            break

# Read data func
def Read_Data():
    read = True
    while read != '3':
        print('\n----Cars Data----\n')
        print('1. Cars Data Report')
        print('2. Report Selected Data')
        print('3. Back to Homepage')
        read = input('Select Options: ')
        if read == '1':
            if len(cars) != 0:
                print('Cars list:')
                for j, i in enumerate(cars):
                    print(f"{j+1}. vin: {i['vin']}, brand: {i['brand']}, model: {i['model']}, year: {i['year']}")
            else:
                print('\n----No data found----')
        elif read == '2':
            if len(cars) != 0:
                std = input('Input VIN: ')
                for j, i in enumerate(cars):
                    if i['vin'] == std:
                        print(f"{j+1}. vin: {i['vin']}, brand: {i['brand']}, model: {i['model']}, year: {i['year']}")
                        break
                else:
                    print('\n----No data found----')
                    create_new = input('VIN not found. Do you want to create a new entry? (yes/no): ')
                    if create_new == 'yes':
                        Create_Data()
            else:
                print('\n----No data found----')
        elif read == '3':
            break

# Update func
def Update_Data():
    update = True
    while update != '2':
        print('1. Update data')
        print('2. Back to Homepage')
        update = input('Choose Options: ')
        if update == '1':
            vin = input('Input VIN: ')
            for i in cars:
                if i['vin'] == vin:
                    print(f"Current data - vin: {i['vin']}, brand: {i['brand']}, model: {i['model']}, year: {i['year']}")
                    upDB = True
                    while upDB:
                        ask = input('Type yes if more updates are needed, and no if done: ')
                        if ask == 'yes':
                            column = input('Input column that you want to update: ')
                            updated_data = input(f"Input new {column}: ")
                            i[column] = updated_data
                            save_as = input('Update data? (yes/no): ')
                            if save_as == 'yes':
                                print('Data updated')
                            else:
                                print('Data has not been updated')
                            askU = False
                        elif ask == 'no':
                            print('Data has not been updated')
                            upDB = False
                    break
            else:
                print('Data not found')
                create_new = input('VIN not found. Do you want to create a new entry? (yes/no): ')
                if create_new == 'yes':
                    Create_Data()
        elif update == '2':
            break

# Delete func
def Delete_Data():
    delete = True
    while delete != '2':
        print('1. Delete data')
        print('2. Back to Homepage')
        delete = input('Choose Options: ')
        if delete == '1':
            vin = input('Input VIN: ')
            for i in cars:
                if i['vin'] == vin:
                    del_confirm = input('Delete data? (yes/no): ')
                    if del_confirm == 'yes':
                        cars.remove(i)
                        print('Data removed')
                        break
                    elif del_confirm == 'no':
                        print('Data has not been removed')
                        break
            else:
                print('Data not found')
                create_new = input('VIN not found. Do you want to create a new data? (yes/no): ')
                if create_new == 'yes':
                    Create_Data()
        elif delete == '2':
            break

# Homepage
def Homepage():
    menu = ['1. Report cars DB', '2. Add cars data', '3. Update Cars data', '4. Delete cars data', '5. Exit']
    options = '0'
    while options != '5':
        print('\n----Cars DB----\n')
        for i in menu:
            print(i)
        options = input('Select Options: ')
        if options == '1':
            Read_Data()
        elif options == '2':
            Create_Data()
        elif options == '3':
            Update_Data()
        elif options == '4':
            Delete_Data()
        elif options == '5':
            exit_confirm = input('Are you sure you want to exit? (yes/no): ')
            if exit_confirm == 'yes':
                print('Goodbye!')
                break
            else:
                options = '0'
        else:
            print('Wrong input')

# Start the program
Homepage()