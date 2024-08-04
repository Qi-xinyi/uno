def judge(card_last, card_first):
    """
    判断上一张牌是否可以跟上一张牌，并返回是否可以跟牌和跟牌后得分。
    
    Args:
        card_last (tuple): 上一张牌的牌面信息，由颜色和数字组成，例如 ('r', '3') 表示红色3。
        card_first (tuple): 当前要出的牌面信息，由颜色和数字组成，例如 ('b', '+2') 表示蓝色加2。
    
    Returns:
        bool类型，表示是否可以跟牌。
    
    """
    if card_last[0]==card_first[0] or card_first[1]==card_last[1]:
        return True
    elif card_last[0]=='+2' and card_first[0]=="+4":
        return True
    elif card_last[1]=="all":
        return True
    else:
        return False


def add(add, card_first,player):
    """
    根据给定条件为玩家添加牌。

    Args:
        add: int类型，需要为玩家添加的牌数。
        card_first: list类型，包含玩家手中第一张牌的数值和花色。
        player: Player类型，需要添加牌的玩家对象。

    Returns:
        int类型，返回0表示添加牌成功。

    Raises:
        无

    注意事项：
        1. 如果需要添加的牌数add为0，则不执行添加操作，直接返回0。
        2. 如果玩家手中第一张牌的花色是'+2'或'+4'，则不执行添加操作，直接返回0。
    """
    if add!=0 and (card_first.name[1]!='+2' or card_first.name[1]!='+4'):
        player.add_cards(add)
        return 0
    else:
        return add

def query(player,n,colour,add,bool_):
    '''
    len(player)==4,colour为card_last.name[2]，n为轮数，add为现有加牌数,bool_为是否是d倒序
    '''
    a=n%4
    d=False
    if bool_:
        b=(n-1)%4
    else:
        b=(n+1)%4
    Q=input("是否要质疑(y/n):")
    if Q=='y':
        for card_ in player[b].card:
            if card_[1]==colour:
                d=True
                break
        if d:
            print('质疑成功')
            player[b].add_cards(4)
        else:
            print('质疑失败')
            if add+6>8:
                add=8
            else:
                add+=6
            player[a].add_cards(add)
    return 0    #赋值给add将add清零