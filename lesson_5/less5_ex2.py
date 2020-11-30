data = open('input.txt', 'r')
f = data.readlines()
n = 0
k = []
for line in f:
    n=n+1
    list1= line.split()
    print(list1)
    k.append(str(len(list1)))
data.close()
print('колическтов строк = {}'.format (n))
print ('количество слов в строках: '+ ','.join(k))

