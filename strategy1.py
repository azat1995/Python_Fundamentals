class Unit():
	"""docstring for Unit"""
	def __init__(self, arg=0, num=0):
		super(Unit, self).__init__()
		self.command = arg
		self.number = num
	def __del__(self):
		#super(Unit,self).__del__()
		print('юнит №{} команды {} убит'.format (self.number, self.command))
class Hero(Unit):
	"""docstring for Hero"""
	exp=0
	level=1
	               
        #def addexp(self):
                #self.exp+=50

	#def level_up(self):
                #self.level+=1
                #self.exp=0
	
class Warrior(Unit):
        hp=20
        dmg=4
        enemy=Hero()
        def hit(self, target):
                target.hp-=self.dmg
                if target.hp<=0:
                        deadth(target)
        def deadth(self):
                if self.hp<=0:
                        self.enemy.exp+=50
                        return 1
                else:
                        return 0
        def gotoHero(self):
                self.dmg+=1
        def warInfo(self):
                return(self.hp, self.dmg)
                
from random import randint as ri

hero1=Hero(1,1)
hero2=Hero(2,1)

com_war1=[]
com_war2=[]

val=ri(1,16)
num1=1
num2=1

for i in range (0, val):
        arg=ri(1,2)
        if arg==1:
                war=Warrior(arg,num1)
                com_war1.append(war)
                num1+=1
        elif arg==2:
                war=Warrior(arg,num2)
                com_war2.append(war)
                num2+=1
for i in com_war1:
        i.enemy=hero2
for i in com_war2:
        i.enemy=hero1
while len(com_war1)!=0 and len(com_war2)!=0:
        com=ri(1,2)
        i=ri(0,len(com_war1))
        j=ri(0,len(com_war2))
        if com==1:
                if i<len(com_war1):
                        if j<len(com_war2):
                                com_war1[i].hit(com_war2[j])
                                if com_war2[j].deadth()==1:
                                        del com_war2[j]
                                        if hero1.exp>=100:
                                                hero1.level+=1
                                                hero1.exp=0
                        else:
                                com_war1[i].gotoHero()
                else:
                        continue
        elif com==2:
                if j<len(com_war2):
                        if i<len(com_war1):
                                com_war2[j].hit(com_war1[i])
                                if com_war1[i].deadth()==1:
                                        del com_war1[i]
                                        if hero2.exp>=100:
                                                hero2.level+=1
                                                her2.exp=0
                        else:
                                com_war2[j].gotoHero()
                else:
                        continue
        for i in com_war1:
                print(i.warInfo())
        print('hero1 level {}, exp {}'.format(hero1.exp, hero1.level))
        for i in com_war2:
                print(i.warInfo())
        print('hero2 level {}, exp {}'.format(hero2.exp, hero2.level))
                
input()  

		
