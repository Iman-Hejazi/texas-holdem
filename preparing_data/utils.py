from constant import Constant as CONST



def display_user_message_for_entering_hand(users):
    if len(users)>=CONST.MIN_PLAYER:
        print(f'Add name and hand of next player or press "s" to start evaluation') 
        print(f'[{len(users)} players - remaining {CONST.MAX_PLAYER-len(users)}]\n') 
    else:
        print(f'Enter name and hand of Player.(if you want to exit, press "q")') 
        print(f'Note: For evaluation, the game needs at least {CONST.MIN_PLAYER} or max {CONST.MAX_PLAYER} players [{len(users)} players - remaining {CONST.MAX_PLAYER-len(users)}]\n') 
