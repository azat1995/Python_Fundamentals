data=open('info.txt', 'r')
lines= data.readlines()
lessons_dict={}
type_list=('(пр)','(л)','(лаб)')
for line in lines:
    lesson=line.split(':')
    lesson[1]=lesson[1].split()
    print (lesson)
    theme=lesson[0]
    hours=0
    for less in lesson[1]:
        for tl in type_list:
            if tl in less:
                less=less.replace(tl, '')

        less=int(less)
        hours+=less
        print(less, type(less))
    ld={theme:hours}
    lessons_dict.update(ld)
print(lessons_dict)

