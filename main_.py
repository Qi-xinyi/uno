import os  
  
def clc():  
    '''clear console'''  
    if os.name == 'nt':  # 检查是否为Windows操作系统  
        os.system('cls')  # 如果是Windows，则执行cls命令清空控制台  
    else:  # 假设不是Windows，则认为是Unix/Linux操作系统  
        os.system('clear')  # 在Unix/Linux中执行clear命令清空控制台  
  
# 省略了部分导入语句...  
  
all_card = all_card.all_card  # 获取所有的牌  
random.shuffle(all_card)  # 随机洗牌  
clc()  # 清空控制台，以便开始新的游戏  
player = [0, 0, 0, 0]  # 初始化玩家列表  
  
# 创建四个玩家，并分发初始牌  
for i in range(4):  
    a_player = input("Player name: ")  # 输入玩家名字  
    seat = int(input("Player seat: (<4)"))  # 输入玩家座位号  
    player1 = Player(a_player, all_card[:8], seat)  # 创建玩家对象，并分发前8张牌  
    all_card = all_card[8:]  # 更新剩余的牌  
    player[player1.seat - 1] = player1  # 将玩家对象添加到玩家列表中  
    a = input(); clc()  # 等待用户输入，然后清空控制台，进行下一个玩家的创建  
  
# 显示每个玩家的名字、座位号和初始牌  
for i in range(4):  
    print(f"{player[i].name},你的座位号是{player[i].seat}你的初始牌是{player[i].card}")  
    a = input(); clc(); a = input()  # 等待用户输入，并清空控制台，显示下一个玩家的信息  
  
# 初始化上一张出的牌和游戏轮数等相关变量  
card_last = Card(all_card[0])  
card_last.name = all_card[0]  
n = 0  # 游戏轮数  
add = 0  # 额外轮数  
bool_ = True  # 游戏进行方向标志  
  
# 游戏主循环  
while True:  
    a = n % 4  # 计算当前应该出牌的玩家索引  
    print(f"第{n + 1}轮，{player[a].name}出牌，上一张牌是{card_last.name}\n你所持有的牌是:", end='\n')  
    # 显示当前玩家的手牌  
    for i in range(0, len(player[a].card)):  
        print(f"{i + 1}:{player[a].card[i]}", end=',')  
    number = int(input("\n请输入出牌号: ")) - 1  # 输入要出的牌的序号  
    if judge.judge(player[a].card[number], card_last.name):  # 判断出牌是否正确  
        print("出牌正确")  
        card_out = Card(player[a].card[number])  # 创建要出的牌对象  
        bool1, add_add, add_turnal = card_out.judge_name()  # 获取出牌结果和额外轮数等信息  
        add = add + add_add  # 累计额外轮数  
        if add > 8:  
            add = 8  # 额外轮数最多为8  
        judge.add(add, card_out, player[a].card)  # 更新牌堆和玩家手牌等信息  
        n = n + add_turnal  # 更新游戏轮数  
        if bool1 == False:  
            bool_ = not bool_  # 改变游戏进行方向  
        if bool_:  
            n = n + 1  # 正向进行游戏轮数增加  
        else:  
            n = n - 1  # 反向进行游戏轮数减少  
        card_out = Card(player[a].card[number])  # 重新创建要出的牌对象，以便后续操作  
        player[a].play_a_card(card_out)  # 玩家出牌，更新手牌等信息