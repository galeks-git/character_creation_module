import math

# Спросим, что хорошего в этой библиотеке.
print(math.__doc__)

# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard.
# 

def we_crash_all(name: str) -> str:    
    return 'Привет, ' + name + ', мы всё сломали!'

print(we_crash_all('100'))