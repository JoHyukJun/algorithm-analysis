'''

    main.py

    Created by JO HYUK JUN on 2022
    Copyright © 2022 JO HYUK JUN. All rights reserved.

'''


def solution(polynomial):
    if len(polynomial) == 0 or polynomial == ' ':
        return '0'
    
    list_p = polynomial.split(' ')
    x_add = 0
    y_add = 0
    
    for val in list_p:
        if val[-1] == 'x':
            if len(val) == 1:
                x_add += 1
            else:
                x_add += int(val[:-1])
        elif val[-1] == '+':
            continue
        else:
            y_add += int(val)
            
    if x_add > 0:
        if x_add == 1:
            if y_add > 0:
                return 'x + ' + str(y_add)
            else:
                return 'x'
        else:
            if y_add > 0:
                return str(x_add) + 'x + ' + str(y_add)
            else:
                return str(x_add) + 'x'
    else:
        if y_add > 0:
            return str(y_add)
        else:
            return '0'