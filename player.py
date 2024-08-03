import all_card

class Player:
    def __init__(self, name, card, seat):
        self.name = name
        self.card = card  # 确保这里传入的card是一个列表
        self.seat = seat

    def play_a_card(self, card_out):
        """出牌"""
        if card_out in self.card:
            self.card.remove(card_out)
        else:
            print("出错了")
            
    def add_cards(self, num_cards):
        """从某个全局或外部定义的牌堆中添加指定数量的牌到玩家手中"""
        import judge_win as jw
        if 0 <= num_cards <= len(all_card.all_card):  # 确保不越界
            card_add = all_card.all_card[:num_cards]
            all_card.all_card = all_card.all_card[num_cards:]  # 更新all_card列表
            self.card.extend(card_add)  # 使用extend来合并列表，而不是+
        else:
            jw.count()  #出错