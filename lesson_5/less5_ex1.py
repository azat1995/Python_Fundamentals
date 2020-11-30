data = open('input.txt', 'w')
info = input('Введите текст\n')
while len(info) > 0:
    data.write(info + '\n')
    info = input()
data.close()
