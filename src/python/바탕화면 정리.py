'''

    main.py

    Created by JO HYUK JUN on 2023
    Copyright © 2023 JO HYUK JUN. All rights reserved.

'''


def solution(wallpaper):
    answer = []
    
    xfile = []
    yfile = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                xfile.append(i)
                yfile.append(j)
                
    answer.append(min(xfile))
    answer.append(min(yfile))
    answer.append(max(xfile) + 1)
    answer.append(max(yfile) + 1)
                
    return answer