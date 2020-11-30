data = open('input.txt', 'r')
f = data.readlines()
n =0
user_list = []
all_zp = 0
for line in f:
    list1 = line.split()
    all_zp += int(list1[1])
    n = n+1
    if int(str(list1[1])) < 20000:
        user_list.append(list1[0])
print (user_list)
data.close
averege_zp = all_zp/n
print('Средний доход:' + str(int(averege_zp)) )
