""" This module calculate  the universal score"""
from constant import Constant as CONST
def calculate_score(hand,hand_value):
    """ Calculate universal score based on the first 5 cards 
        Note: if the fifth card is Ace, in case of stright Ace,2,3,4,5; it convert the Ace to -1 for 
        having consistant score,
        Then it calls the calculate_score_pairs to find the universal value.
    """
    first,second,third,fourth,fifth,*_=[rank for rank,suit in hand]
    if fifth==12:
        fifth=-1
    return calculate_score_pairs(hand_value,first,second,third,fourth,fifth)   
def calculate_score_pairs(hand_value,*args):
    """ Calculate universal score
        This function first, divide each card by a specefic ratio, in order, then 
        sum of cards will added to hand_value (specefic value for each hand for example Flush has 500 score )
    """
    # ratios=[1,10,100,1000,10000]
    ratios = CONST.RATIOS[:]
    return sum(map(lambda a,b:a/b, args, ratios))+hand_value