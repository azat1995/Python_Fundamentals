data=open('input.txt', 'r')
lines = data.readlines()
data.close()
eng_nums=['One', "Two", 'Three', 'Four']
rus_nums=['Один', 'Два', 'Три', 'Четыре']
data =open('output.txt', 'w')
n=0
for line in lines:
    print (n, line)
    line=line.replace(eng_nums[n], rus_nums[n])
    n += 1
    data.write(line)
data.close()
