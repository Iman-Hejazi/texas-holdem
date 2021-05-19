import sys
from preparing_data.preparing_data import preparing_community,preparing_player_hand
from preparing_data.utils import display_user_message_for_entering_hand
from constant import Constant as CONST



def reading_data_from_consol():
        community_cards=[]
        players=[]
        start_evaluation=False
        print('Please Enter Community Cards')
        for line in sys.stdin:

            if line.rstrip() in 'qQ':
                break
    
            if (len(players)==CONST.MAX_PLAYER) or (line.rstrip() in 'sS' and len(players)>=CONST.MIN_PLAYER ):
                start_evaluation=True
                break
            elif not community_cards:
                community_cards=preparing_community(line.strip())
                if community_cards:
                    print('\nThe community cards are added')
                    display_user_message_for_entering_hand(players)
                else:
                    print("(if you want to exit, press 'q')")
            elif community_cards :
                
                is_valid_player=preparing_player_hand(community_cards,line.strip())
                if is_valid_player:
                    name = is_valid_player['name']
                    print(f'\n{name} added')
                    players.append(is_valid_player)  
                    display_user_message_for_entering_hand(players)
                else:
                    print("Please enter again:")
        return start_evaluation,players