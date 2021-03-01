'''

    main.py

    Created by JO HYUK JUN on 2021
    Copyright © 2021 JO HYUK JUN. All rights reserved.

'''


from typing import TypeVar

T = TypeVar('T')

def po(x: T) -> int:
    return x + 1

print(po(1))
print(po(1.09))