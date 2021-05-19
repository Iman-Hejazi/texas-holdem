from constant import Constant as CONST
from custom_exception.custom_exception import CustomError

CARDS = {   "S":[],
            "H":[],
            "D":[],
            "C":[]
        }


def preparing_community(cards):
    """Validation and preperation, user input for community"""
    converted_community=[]
    cards=cards.split()
    if len(cards) != 5:
        print(f'The Community cards are not valid. (e.g. Acceptable Format: "KS AD 3H 7C TD" )')
        return False
    for card in cards:
        card=card.upper()
        if not check_card(card):
            reset_CARDS()
            return False
        converted_community.append((findIndex(CONST.RANKS,card[0]),findIndex(CONST.SUITS,card[1])))
    return converted_community



def preparing_player_hand(community,hands):
    """Validation and preparation, user input for hand"""
    
    converted_hand=[]
    hands=hands.split()
    if len(hands) != 3:
        print(f'The player"s hand is not valid. (e.g. Acceptable Format: "Sam AC KH" )')
        return False
    for card in hands[1:]:  
        card=card.upper() 
        if not check_card(card):
            delete_inserted_card_to_CARDS( hands[1])
            return False
        
        converted_hand.append((findIndex(CONST.RANKS,card[0]),findIndex(CONST.SUITS,card[1])))
    
    complete_hand = community[:]
    complete_hand.extend(converted_hand)
    name = hands[0]
    
    return  creating_player_dict(complete_hand,name)

def creating_player_dict(hand,name):
    player=dict()
    sorted_hand =sorted(hand,reverse=True,key=lambda x:x[0])
    player["name"] = name
    player["hand"] = sorted_hand
    return player
    
def check_card(card):
    """Check general validation and at the end, check if this card already inserted"""
    if len(card)!=2:
        print(f'This Card {card} is not valid. (e.g. Acceptable Format: QC )')
        return False
    
    if not card[0] in CONST.RANKS:
        print(f'The rank/face of this card {card} is not valid. (e.g. Acceptable Formats: "2-3-4-5-6-7-8-9-T-J-Q-K-A")')
        return False
    if not card[1] in CONST.SUITS:
        print(f'The suit of this card {card} is not valid. (e.g. Acceptable Formats: "S" "H" "D" "C")')
        return False
    if not check_is_valid_card(card):
        print(f'This card {card} has already been inserted.')
        return False
    return True

def check_is_valid_card(card):
    """check if this card has been already inserted"""
    if  card[0] in CARDS[card[1]]:
        return False
    CARDS[card[1]] = CARDS.get(card[1], []) + [card[0] ]
    return True

def reset_CARDS():
    """Reseting CARDS for bad user input"""
    for key in CARDS.keys():
        CARDS[key]=[]

def delete_inserted_card_to_CARDS(card):
    for key in CARDS.keys():
        if card[0] in CARDS[key]:
            CARDS[key].remove(card[0])

def findIndex(s,char):
    """Find index of each rank or suit to map to the pattern"""
    return s.index(char)



#  helper functions for file

def creating_players_hand(lines):
    players=[]
    community_cards = creating_community(lines[0])
    i=2
    for hand in lines[1:]:
        is_valid_player = preparing_player_hand(community_cards,hand)
        if not is_valid_player:
            raise CustomError(f'Line: {i}: {hand} ')
        players.append(is_valid_player)
        i+=1
    return players
    

def creating_community(cards):
    community_cards=[]
    community_cards=preparing_community(cards)
    if not  community_cards:
         raise CustomError(f'Line 1: {cards}')
    return community_cards