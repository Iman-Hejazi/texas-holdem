""" This module has all logic to find value of hands"""
from constant import Constant as CONST

def check_straight(cards):
    """ checking if the given hand is stright or  not
        This function iterate through 14 cards and check if each
        card exists in the given hand => if exist it adds that card to the straight_set
        if does not exist it resets the straight_set
        if we have five cards in the straight_set, it means we have a stright hand"""
    all_ranks= CONST.RANKS_LIST[:]
    numbers=[ rank for rank,suit in cards]
    straight_set=[]
    for rank in all_ranks:
        if rank in numbers:
            straight_set.append(cards[numbers.index(rank)])
            if len(straight_set)==5:
                return straight_set
        else:
            straight_set=[] 

    # we should check Ace for converting to 1 => if the length of straight_set is four
    if len(straight_set)==4 and straight_set[3][0]==0 and 12 in numbers:
        straight_set.append(cards[0])
        return straight_set
    return False


# Flush
def most_frequent_suit(List):
    """ Calculate the most frequent suit in the given hand """
    suits=[suit for rank,suit in List]
    most_frequent=max(set(suits), key = suits.count)
    return most_frequent,suits.count(most_frequent)

def check_flush(cards):
    """ checking the given hand is Flush or  not """
    common_suit,num_of_times=most_frequent_suit(cards)
    if num_of_times >=5:
        return list(filter(lambda x: x[1] == common_suit, cards))
    return False


def find_all_combinations_of_pairs(cards):
    """ Finding all combination of cards for detecting the pairs
        First this function creates a dictionary to find the occurance of each card.
        for all possible combinations, I create three lists.
        Then by iterating through dictionary,
        based on the value of each card, it adds the cards to the
        target list. Finally, it returns all three lists"""
    numbers=[ rank for rank,suit in cards]
    occurence = dict()
    for num in numbers:
        occurence[num]= occurence.get(num, 0)+1    
    ######################
    four_of_kind=[]
    three_of_kind=[]
    two_of_kind=[]
    for key,value in occurence.items():
        if value == 4:
            four_of_kind.append(key)
            break
        if value == 3:
            three_of_kind.append(key)
        if value == 2:
            two_of_kind.append(key)   
    return four_of_kind,three_of_kind,two_of_kind