#以下适用于Windows系统
'''必要准备'''
global_t=1       #初始为正向
card_last=[]
card_now=[]     #定义在场起作用的两张牌
n=0

# def turn(n):
#     n=n%4
#     return n

colour_may=['r','y','b','g']         #可能出现的颜色
number=list(range(0,10))
func=['T','S',"all"]

'''备牌 -> 洗牌 -> 发牌'''
all_card=[[1, 'r'], [1, 'y'], [1, 'b'], [1, 'g'], [2, 'r'], [2, 'y'], [2, 'b'], \
    [2, 'g'], [3, 'r'], [3, 'y'], [3, 'b'], [3, 'g'], [4, 'r'], [4, 'y'], [4, 'b'],\
    [4, 'g'], [5, 'r'], [5, 'y'], [5, 'b'], [5, 'g'], [6, 'r'], [6, 'y'], [6, 'b'],\
    [6, 'g'], [7, 'r'], [7, 'y'], [7, 'b'], [7, 'g'], [8, 'r'], [8, 'y'], [8, 'b'], \
    [8, 'g'], [1, 'r'], [1, 'y'], [1, 'b'], [1, 'g'], [2, 'r'], [2, 'y'], [2, 'b'],\
    [2, 'g'], [3, 'r'], [3, 'y'], [3, 'b'], [3, 'g'], [4, 'r'], [4, 'y'], [4, 'b'],\
    [4, 'g'], [5, 'r'], [5, 'y'], [5, 'b'], [5, 'g'], [6, 'r'], [6, 'y'], [6, 'b'],\
    [6, 'g'], [7, 'r'], [7, 'y'], [7, 'b'], [7, 'g'], [8, 'r'], [8, 'y'], [8, 'b'],\
    [8, 'g'], [8, 'r'], [8, 'y'], [8, 'b'], [8, 'g'],['T', 'r'], ['T', 'y'], ['T', 'b'],\
    ['T', 'g'], ['S', 'r'], ['S', 'y'], ['S', 'b'], ['S', 'g'], ['+2', 'r'], ['+2', 'y'],\
    ['+2', 'b'], ['+2', 'g'], ['T', 'r'], ['T', 'y'], ['T', 'b'], ['T', 'g'], ['S', 'r'],\
    ['S', 'y'], ['S', 'b'], ['S', 'g'], ['+2', 'r'], ['+2', 'y'], ['+2', 'b'],\
    ['+2', 'g'], ['+4', 'all'], ['all', 'all'], ['+4', 'all'], ['all', 'all'], \
    [0, 'b'], [0, 'g'], [0, 'y'], [0, 'r']]

import random   #洗牌
random.shuffle(all_card)
print(all_card)

player1=[]
player2=[]
player3=[]
player4=[]
player=[player1,player2,player3,player4]

import os
print(0)
os.system('cls')

for i in range(0,4):#分牌
    player[i]=all_card[0:7]
    del all_card[0:7]
    print("player"+str(i+1),end=":")
    os.system("pause")
    print(str(player[i]))
    os.system("pause")
    os.system('cls')

'''胜利判定'''
def uno(n):
    '''判定uno'''
    a=n%4
    if len(player[a])==1:
        print("uno")
            
def win(n):
    '''判定胜利'''
    a=n%4
    if len(player[a])==0:
        print("player"+str(a+1)+"is win")
        global global_t
        global_t=1000
        return "break"     #使用eval()使游戏循环停止,t=1000时可以调用_break()
    else:
        return ""

def _win():
    '''解决牌发完的问题,每次发牌结束后调用'''
    n_win=[]
    if len(all_card)==0:
        for i in range(0,4):
            n_win[i]=len(player(i))
        _win_max=max(n_win)
        a=n_win.index(_win_max)
        print("player"+str(a+1)+"is win")
        global global_t
        global_t=1000
        return "break"      #使用eval()使游戏循环停止,1000赋值给t,t=1000时可以调用_break() 
    else:
        return ""
    
'''结束'''

'''特殊牌的规则函数'''

def stop(n):
    '''禁止牌'''
    if global_t>0:
        n=n+1
    else:
        n=n-1
    return n

def _T():
    '''反方向'''
    global global_t
    global_t=-global_t       #t初始为正，代表以1，2，3，4为序；若t为负，代表以4，3，2，1为序

def all_colour():
    '''黑色牌指定颜色'''
    t=1
    while t==1:
        colour=input()
        if colour in colour_may:
            t=0
    card_now[1]=colour

def _add(n,add):
    '''加牌(包括“+4”和“+2”，以n决定加的具体数量,返回值给add)'''
    a=n%4
    global player
    for i in range(0,add):
        player[a].append[all_card[0]]
        del all_card[0]
    return 0

def add1(n):
    '''无牌可出'''
    global card_last
    global card_now
    a=n%4
    s=str(input("unable"))
    if s=="unable":
        _add(n,1)
        card_now=player[a][-1]
        if judge_all(n,0):
            del player[a][-1]
        else:
            card_now=card_last
        return 0
    else:
        return 1
    
# def add_2():
#     '''+2牌的处理'''
    
# def add_4():
#     '''+4牌的处理'''

# def add_total():
#     '''加牌总数'''

def query(n,colour,add):
    '''质疑:a为质疑者序列号，b为被质疑者序列号'''
    global player
    a=n%4
    if global_t>0:
        b=a-1
    else:
        if a==3:
            b=0
        else:
            b=a+1
    for i in player[b]:
        if i[1]==card_last[1]:
            print("You are right")
            add==0
            break
        else:
            if add>6:
                _add(a,8)
            else:
                add=add+6
                _add(a,add)
            add=0
            
        
'''结束'''

#用作调试
# print(str(player1))
# os.system("pause")
# _add('1',2)
# os.system('cls')
# os.system("pause")
# print(str(player1))

'''制定出牌规则'''

def special(n):          
    '''对特殊牌操作，judge()内部使用'''
    global global_t
    if card_now[1]=="all":     #多功能牌
        all_colour()
    elif card_now[0]=='T':
        _T()
    elif card_now[0]=='S':
        stop(n)
    return True
    
def add24(add):
    '''add<8时使用，+2,+4牌，judge()内部当card_last==+2使用'''
    if card_now=="+2":
        add=add+2
    elif card_now=="+4":
        add=add+4
    else:
        return False, add
    if add>8:
        add=8
    return True, 8

def add4(add):
    '''add<8时使用，+4牌，judge()内部当card_last==+4使用'''
    if card_now[1]=="+4":
        add=add+4
    else:
        return False, add
    if add>8:
        add=8
    return True, add
    

def judge_normal(n):
    '''判断是否合理,if card_now[0] in number'''
    global card_last
    global card_now
    if card_now[1]==card_last[1] or card_last[0]==card_now[0]:
        return True
    else:
        return False
    
def judge_all(n,add):
    '''判断所有情况'''
    global card_last
    global card_now
    
    if card_last[0]=='+2':
        if card_now[0]!='+2' and card_now[0]!=card_now[0]!=+4:
            return False
    elif card_last[0]=='+4':
        return False
    if card_now[0] in number:
            _bool=judge_normal(n)
    elif card_now[0] in func:
            _bool=special(n)
    else:
            if (card_now[0]=="+4" or card_now[0]=="+2") and add<8:
                    _bool,add=add24(add)
            elif card_last[0]=="+4":
                    _bool,add=add4(add)
            else:
                    return False
            _add(n,add)
            return True

def _continue(n):
    '''n++'''
    if global_t>0:     #正序
        n=n+1
    else:       #倒序
        n=n-1
        
'''结束'''

'''指示出牌'''

# def turn(n):            #a为turn(n)
#     '''出牌'''
#     a=n%4
#     print("It's player"+str(a+1)+"\'s turn")
#     t=1
#     while t==1:
#         b=eval(input("Please enter the cards played"))      #请输入所出牌
#         if b in player[a]:
#             player[a].remove(b)
#             t=0
#         return b       #放入判断，judge()函数，作为card_now              
  
def first():
    '''判断第一个出牌者,双返回值，返回首牌和首出牌人'''
    global card_now
    global card_last
    C=[]
    N=[]
    for i in range(0,4):
        t=1
        while t==1:    
            if all_card[0][0] in number:
                N.append(all_card[0][0])    #存数
                C.append(all_card[0])       #存牌
                t=0  
            del all_card[0]
    a=max(N)
    n=N.index(a)
    card_last=C[n]
    return n,C[n]

def card_print(n):
    '''输出card_last和player[n]'''
    a=n%4
    print(card_last)
    print(player[a])

def play_a_hand(n,add):
    '''出牌'''
    a=n%4
    t1=1
    global card_now
    r=int(input("Please output the card number:"))       #请输出所出牌序号：
    t=0
    if r>len(player[a]):
        print("r is too large")
        t=1
    while not (judge_all(n,add)):
        t=1
        while t==1:
            r=int(input("Please output the card number:"))       #请输出所出牌序号：
            t=0
            if r>len(player[a]):
                print("r is too large")
                t=1
        card_now=player[a][r-1]

'''结束'''

'''
正式开始
1、首先显示该玩家持有所有卡牌和card_last并检查是否需要加牌。
2、通过列表序列号实现出牌。
3、判定是否为特殊牌。
4、与card_last进行匹配。
5、匹配成功。
6、若失败，返回第二步。
7、删除所出牌。
8、判断uno或win。
9、清空界面。
'''

n,card_last=first()
add=0

while True:     #依靠eval(win())和eval(_win())函数结束循环
    if _win()!="":
        eval(_win())
    if card_last[1]=='+4':
        s=input("Do you have doubts?")
        if s=="yes":
            query(n,card_last[1],add)
    card_print(n)
    t=1
    while t==1:
        card_now=play_a_hand(n,add)
        if judge_all:
            del all_card[0]
            player[n%4].remove(card_now)
            t=0
        else:
            t=add1(n)
    uno(n)
    if win()!="":
        eval(win())