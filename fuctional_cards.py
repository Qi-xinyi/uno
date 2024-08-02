def function_judge1(card_first):
    '''三返回值，第一个是判断是否是正序，第二个是判断是否是加牌，第三个用于判断是否跳过'''
    # 如果上一张牌是倒序牌
    if card_first[1]=='T':
        # 返回False，0，表示不是正序，不是加牌，不跳过
        return False,0
    # 如果上一张牌是+2牌
    elif card_first[1]=='+2':
        # 返回True，2，1，表示是正序，+2牌，需要跳过
        return True,2,1
    # 如果上一张牌是+4牌
    elif card_first[1]=='+4':
        # 返回True，4，1，表示是正序，+4牌，需要跳过
        return True,4,1
    # 如果上一张牌是停止牌
    elif card_first[1]=='S':
        # 返回True，0，1，表示是正序，不是加牌，需要跳过
        return True,0,1
    else:
        # 其他情况返回True，0，0，表示是正序，不是加牌，不跳过
        return True,0,0
    
colour=['r','g','b','y']

def fuction_judge0(card_first):
    '''返回值是颜色，如果用户输入的不是颜色，则给出提示并继续循环'''
    if card_first[0]=='all':
        colour_chose=0
        while True:
            colour_chose=input("请输入颜色：")
            if colour_chose in colour:
                # 如果用户输入了一个有效的颜色，则跳出循环
                break
            else:
                # 如果用户输入的不是有效颜色，则给出提示并继续循环
                print("无效的颜色选择，请重新输入。")
            return colour_chose