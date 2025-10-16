RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

def japan_flag():
    line = ' ' *1
    length = 45
    height = 12
    for i in range(height):
        if 5 <= i <= 6:
            print(f'{WHITE}{line * 15}{RED}{line * 15}{WHITE}{line * 15}{END}')
        elif i == 4 or i == 7:
            print(f'{WHITE}{line * 17}{RED}{line * 11}{WHITE}{line * 17}{END}')
        elif i == 3 or i == 8:
            print(f'{WHITE}{line * 19}{RED}{line * 7}{WHITE}{line * 19}{END}')
        else:
            print(f'{WHITE}{line * 45}{END}')

japan_flag()        