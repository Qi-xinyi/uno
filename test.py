import os

def clc():
    '''clear console'''
    if os.name == 'nt':  # 检查是否为Windows
        os.system('cls')
    else:  # 假设不是Windows，则使用Unix/Linux命令
        os.system('clear')

# import card as c
import random
import all_card
from player import Player
from card import Card
import judge

all_card=all_card.all_card
random.shuffle(all_card)
clc()
player=[0,0,0,0]
player=[Player(1,all_card[:8],1),Player(1,all_card[8:16],2),Player(3,all_card[16:24],3),Player(4,all_card[24:32],4)]
all_card=all_card[24:]

for i in range(4):
    print(f"{player[i].name},你的座位号是{player[i].seat}你的初始牌是{player[i].card}")
    a=input();clc();a=input()

card_last=Card(all_card[0])
card_last.name=all_card[0]
n=0
add=0


while True:
    a=n%4
    print(f"第{n+1}轮，{player[a].name}出牌，上一张牌是{card_last.name}\n你所持有的牌是:",end='\n')
    for i in range(0,len(player[a].card)):
        print(f"{i+1}:{player[a].card[i]}",end=',')
    number=0
    if judge.judge(player[a].card[number],card_last.name):
        print("出牌正确")
        _bool,add_add,add_turnal=card_out.judge_name()
        card_out=Card(player[a].card[number])
        player[n%4].play_a_card(card_out)
        n=n+1