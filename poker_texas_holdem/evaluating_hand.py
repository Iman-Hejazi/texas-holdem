# from utils import find_real_name
from .utils import find_real_name,find_max
from .calculate_score import   calculate_score,calculate_score_pairs
from .finding_hand_value import check_straight,check_flush,find_all_combinations_of_pairs
from constant import Constant as CONST



def evaluating_hand(sorted_card):
    # 1: check for royal flash and stright flash:
    is_flush= check_flush(sorted_card)
    is_straight = check_straight(sorted_card)

    if is_flush and is_straight:
        is_straight_flush = check_straight(is_flush)
        if is_straight_flush:
            if is_straight_flush[0][0]==12:
                return {"score":CONST.ROYAL_FLUSH,"hand_value":"Royal flush"}
            else:
                score = calculate_score(is_straight,CONST.STRIGHT_FLUSH)
                return {"score":score,"hand_value":f'Straight flush {find_real_name(is_straight_flush[0][0])}'}
   
    # this funciton return all possible combination of pairs          
    four_of_kind,three_of_kind,two_of_kind = find_all_combinations_of_pairs(sorted_card)            
   
    # check for of a kind:
    if four_of_kind:
        kiker=find_max(sorted_card,four_of_kind,1)
        score = calculate_score_pairs(CONST.FOUR_OF_KIND,four_of_kind[0] ,four_of_kind[0] ,four_of_kind[0] ,four_of_kind[0] ,kiker[0])   
        return {"score":score,
                "hand_value":f'Four of a Kind {find_real_name(four_of_kind[0])} ',
                "kickers":find_real_name(kiker[0])}
    
    # Full house
    elif three_of_kind and two_of_kind :
        three_kind_value = max(three_of_kind)
        pair_value = max(two_of_kind)    
        score = calculate_score_pairs(CONST.FULL_HOUSE,three_kind_value,three_kind_value,three_kind_value,pair_value,pair_value)
        hand_value =f'Full house,three of a kind {find_real_name(three_kind_value)} and a pair of {find_real_name(pair_value)} '
        return {"score":score,"hand_value":hand_value}
    elif len(three_of_kind) == 2:
        three_kind_value = max(three_of_kind)
        pair_value = min(three_of_kind)
        score = calculate_score_pairs(CONST.FULL_HOUSE,three_kind_value,three_kind_value,three_kind_value,pair_value,pair_value)
        hand_value =f'Full house,three of a kind {find_real_name(three_kind_value)} and a pair of {find_real_name(pair_value)} '
        return {"score":score,"hand_value":hand_value}
    
    # Flush
    elif is_flush:
        score = calculate_score(is_flush,CONST.FLUSH)
        flush_kickers=list(map(find_real_name,[rank for rank,suit in is_flush]))
        return {"score":score,"hand_value":f'Flush, High Card {flush_kickers[0]}',"kickers":flush_kickers[1:]}
    
    # Stirght
    elif is_straight:
        score = calculate_score(is_straight,CONST.STRIGHT)
        straight_kickers=list(map(find_real_name,[rank for rank,suit in is_straight]))
        return {"score":score,"hand_value":f'Straight {straight_kickers[0]}'}
    
    # Three of a Kind
    elif three_of_kind:
        first,second=find_max(sorted_card,three_of_kind,2)
        max_rank= max(three_of_kind)
        score = calculate_score_pairs(CONST.THREE_OF_KIND,max_rank,max_rank,max_rank,first,second)
        hand_value =f'Three of a kind {find_real_name(max(three_of_kind))} '
        return {"score":score,"hand_value":hand_value,"kickers":f'{find_real_name(first), find_real_name(second)}'}
   
    # Two Pair
    elif len(two_of_kind) >= 2:
        two_of_kind.sort(reverse=True)
        kiker=find_max(sorted_card,two_of_kind,1)
        score = calculate_score_pairs(CONST.TWO_PAIR,two_of_kind[0],two_of_kind[0],two_of_kind[1],two_of_kind[1],kiker[0])
        hand_value = f'Two Pair  {find_real_name(two_of_kind[0])}, {find_real_name(two_of_kind[1])} '
        return {"score":score,"hand_value":hand_value,"kickers":find_real_name(kiker[0])}
   
    # One Pair
    elif len(two_of_kind) == 1:  
        first,second,third = find_max(sorted_card,two_of_kind,3)
        score = calculate_score_pairs(CONST.PAIR,two_of_kind[0],two_of_kind[0],first,second,third)
        hand_value =f'Pair {find_real_name(two_of_kind[0])} '
        return {"score":score,"hand_value":hand_value,"kickers":f'{find_real_name(first), find_real_name(second) , find_real_name(third)}'}
    
    # High Card
    else:
        score = calculate_score(sorted_card,CONST.HIGH_CARD)
        high_cards_kickers=list(map(find_real_name,[rank for rank,suit in sorted_card[:5]]))
        return {"score":score,"hand_value":f'High Card {high_cards_kickers[0]}',"kickers":high_cards_kickers[1:]} 







                
