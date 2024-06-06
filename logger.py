from data_create import name_data, surname_data, phone_data, adress_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"Вариант 1: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"Вариант 2: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберите наиболее удобный вариант: "))
    
    while var != 1 and var != 2:
        print ("Неверный ввод")
        var = int(input('Введите число  '))

    if var == 1:
        with open('data1.csv',  'a', encoding='utf-8') as f:  
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data2.csv',  'a', encoding='utf-8') as f:  
            f.write(f"{name}; {surname}; {phone}; {adress}\n\n")

def print_data():
    print ('Вывожу данные из 1 файла: \n')
    with open('data1.csv',  'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
               data_first_list.append(''.join(data_first[j:i+1]))
               j = i
        print(''.join(data_first_list))

    print ('Вывожу данные из 2 файла: \n')
    with open('data2.csv',  'r', encoding='utf-8') as f: 
        data_second = f.readlines()
        print(*data_second)

print_data()


