import os
import all_card

def clc():
    '''clear console'''
    if os.name == 'nt':  # 检查是否为Windows
        os.system('cls')
    else:  # 假设不是Windows，则使用Unix/Linux命令
        os.system('clear')

from player import Player
from card import Card
import judge
import judge_win as jw

t=True  #判断是否正常结束

def count_card(player):
    """
    统计玩家手牌数量。
    
    Args:
        player (list): 玩家列表，需要包含name和card属性。
    
    Returns:
        None
    
    """
    for i in range(4):
        print(f'{player[i].name}有{len(player[i].card)}张牌')


def add_one(player):
    """
    给玩家增加一张牌并打印玩家手牌。
    
    Args:
        player (Player): 玩家对象，需要包含add_cards方法和card属性。
    
    Returns:
        None
    
    """
    a=input("是否要加一张牌(y/n): ")
    if a=='y':
        player.add_cards(1) #加一张牌
        for i in range(0,len(player.card)): 
            print(f"{i+1}:{player.card[i]}",end=',')    #重新打印玩家手牌
        t=3
    else:
        t=2
    return t

clc()
player=[0,0,0,0]
for i in range(4):
    a_player=input("Player name: ")
    seat=int(input("Player seat: (<4)"))
    player1=Player(a_player,all_card.all_card[:8],seat)
    all_card.all_card=all_card.all_card[8:]
    player[player1.seat-1]=player1
    a=input();clc() #等待后清空界面

for i in range(4):
    print(f"{player[i].name},你的座位号是{player[i].seat}你的初始牌是{player[i].card}")
    a=input();clc();a=input()

card_last=Card(all_card.all_card[0])
card_last.name=all_card.all_card[0]
all_card.all_card=all_card.all_card[1:]

colour='0'
n=0 #n%4为当前玩家编号
add=0   #累计加数
bool_=True  #判断是否是倒序

while True:
    if len(all_card.all_card)==0:
        print("游戏结束")
        t=False #非正常结束
        break
    a=n%4   #当前玩家编号
    print(f"{player[a].name}出牌，上一张牌是{card_last.name}\n你所持有的牌是:",end='\n')
    count_card(player)  #统计玩家手牌数量
    
    if card_last.name[0]=='+4':   #判断是否可以质疑
        add=judge.query(player,n,colour,add,bool_)  #质疑玩家手牌
        
    for i in range(0,len(player[a].card)):
        print(f"{i+1}:{player[a].card[i]}",end=',') #打印玩家手牌
        
    t=add_one(player[a])  #询问是否要加一张牌
    if t==3:
        t=input('是否要跳过出牌(y/n): ')    #跳过出牌的选项
        if t=='y':
            judge.add(add,card_out,player[a])  #将牌加到玩家手中
            if bool_:   #进入下一人
                n=n+1
            else:
                n=n-1
            continue
    
    try:
        number=int(input("\n请输入出牌号: "))-1
        player[a].card[number]   #判断输入的牌是否在玩家手中
    except:
        print("输入错误")   #如果输入错误，则跳出循环
        continue
    if judge.judge(player[a].card[number],card_last.name):
        print("出牌正确")   #判断牌是否可以出
        card_out=Card(player[a].card[number])   #将牌放入card_out
        
        bool1,add_add,add_turnal=card_out.judge_name()  #判断出牌是否为功能牌，返回一个布尔值，加点数和加轮数
        add=judge.add(add,card_out,player[a])  #将牌加到玩家手中
        add=add+add_add #加牌数
        if add>8:   #如果加牌数大于8，则将加牌数变为8
            add=8
        n=n+add_turnal#跳人
        if bool1==False:    #如果是'T'，则将bool_置反
            bool_=not bool_
        if bool_:   #进入下一人
            n=n+1
        else:
            n=n-1
        
        player[a].play_a_card(card_out.name)     #将牌从玩家手中移除
        if card_out.name[1]=='all':
            while True:
                a=input("请输入颜色(g,b,y,r)：")
                if a in ['g','b','y','r']:
                    card_out.name[1]=a
                    break
                else:
                    print("输入错误")
        colour_last=card_last.name[1]  #更新上一张牌
        card_last=card_out  #使用完毕的牌更新为上一张牌
        
        jw.check_uno(a,player)   #判断是否是Uno
        turn=jw.win(a,player)#判断是否胜利
        if turn=='continue':
            input();clc();input();continue
            # continue
        else:
            break
        
if t==False:   #如果非正常结束，则跳出循环
    score=[0,0,0,0] #记录个人得分
    for i in range(4):
        for t in player[i].card:
            score_=jw.count(player[i].card)
            score[player[i].seat]=score[player[i].seat]+score_
        print(f"{player[i].name}得分：{player[i].score}")
        
    name=[0,1,2,3]  #判断胜利者名字
    for i in range(4):
        name[player[i].seat]=player[i].name
    dict=zip(score,name)
    a=max(score)
    winner=dict[a]
    print(f"游戏结束，{winner}胜利")