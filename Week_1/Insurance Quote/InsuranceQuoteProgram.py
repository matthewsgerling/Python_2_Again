if __name__ == '__main__':

    C_Cost = 0

    D_Name = str(input("What is the name of the Driver: "))
    try:
        D_Age = int(input('What is the age of the Driver: '))
    except ValueError:
        print('Variables not in right format')
        quit(1)
    Coverage = str(input('What is the coverage level:(SM, L, F) '))

    customer_dict = {
        "Name": D_Name,
        "Age": D_Age,
        "Coverage": Coverage,
        "Coverage Cost": C_Cost
    }
    coverage_list_SM = {
        16: 2593,
        25: 608,
        35: 552,
        45: 525,
        55: 494,
        65: 515
    }
    coverage_list_L = {
        16: 2957,
        25: 691,
        35: 627,
        45: 596,
        55: 560,
        65: 585
    }
    coverage_list_F = {
        16: 6930,
        25: 1745,
        35: 1564,
        45: 1469,
        55: 1363,
        65: 1402
    }

    if Coverage == 'SM':
        if (16 <= D_Age <= 24):
            C_Cost = coverage_list_SM[16]
        elif 25 <= D_Age <= 34:
            C_Cost = coverage_list_SM[25]
        elif 35 <= D_Age <= 44:
            C_Cost = coverage_list_SM[35]
        elif 45 <= D_Age <= 54:
            C_Cost = coverage_list_SM[45]
        elif 55 <= D_Age <= 64:
            C_Cost = coverage_list_SM[55]
        elif D_Age >= 65:
            C_Cost = coverage_list_SM[65]
    elif Coverage == 'L':
        if 16 <= D_Age <= 24:
            C_Cost = coverage_list_L[16]
        elif 25 <= D_Age <= 34:
            C_Cost = coverage_list_L[25]
        elif 35 <= D_Age <= 44:
            C_Cost = coverage_list_L[35]
        elif 45 <= D_Age <= 54:
            C_Cost = coverage_list_L[45]
        elif 55 <= D_Age <= 64:
            C_Cost = coverage_list_L[55]
        elif D_Age >= 65:
            C_Cost = coverage_list_L[65]
    elif Coverage == 'F':
        if 16 <= D_Age <= 24:
            C_Cost = coverage_list_F[16]
        elif 25 <= D_Age <= 34:
            C_Cost = coverage_list_F[25]
        elif 35 <= D_Age <= 44:
            C_Cost = coverage_list_F[35]
        elif 45 <= D_Age <= 54:
            C_Cost = coverage_list_F[45]
        elif 55 <= D_Age <= 64:
            C_Cost = coverage_list_F[55]
        elif D_Age >= 65:
            C_Cost = coverage_list_F[65]

    print(customer_dict)
