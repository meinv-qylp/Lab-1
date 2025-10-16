BLACK = '\u001b[40m'
END = '\u001b[0m'

def graph():
    length = 13
    height = 7
    for j in range(height):
        line = ''
        for i in range (length):
            if (i + j == 3) or (i + j == 9) or\
                (i + j == 15) or (i - j == -3) or\
                (i - j == 3) or (i - j == 9):
                line += f'{BLACK}  {END}'
            else:
                line += '  '
        print(line)
                
graph()