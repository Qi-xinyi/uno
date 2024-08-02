def check_uno(n, player):
    '''检查当前玩家是否达到了UNO状态（即只剩一张牌）'''
    # 假设player是一个列表的列表，其中player[n]是当前玩家的手牌
    if len(player[n]) == 1:
        print("uno")
    else:
        pass  # 如果不需要特别处理非UNO情况，可以简单地使用pass

# 示例用法
# 假设有四个玩家，每个玩家的手牌是一个列表
        

def win(n,player):
    """
    判断游戏胜利
    
    Args:
        n (int): 当前轮数
        player (list): 玩家列表，包含四个列表，分别代表四个玩家的牌
    
    Returns:
        str: 返回"break"表示游戏结束，返回"continue"表示游戏继续
    
    """
    '''判定胜利'''
    global t
    a=n%4
    if len(player[a].card)==0:
        print(f"玩家{player[a].name}赢了")
        return "break"     #使用eval()使游戏循环停止
    else:
        return "continue"

def count(player_card):
    '''牌发完了'''
    score=0
    number=[0,1,2,3,4,5,6,7,8,9]
    F=['T','S','+2']
    for i in player_card:
        if i[0] in number:
            score=score+i[0]
        elif i[0] in F:
            score=score+20
        else:
            score=score+50
    score=-score
    return score