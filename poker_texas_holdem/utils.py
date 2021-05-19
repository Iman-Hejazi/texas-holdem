""" This module has two helper funciton"""
from constant import Constant as CONST

def find_real_name(num):
    """Convert the given rank/face to real rank/face """
    
    real_name=CONST.RANKS[num]
    if   real_name in CONST.MAPPING_RANKS:
        return CONST.MAPPING_RANKS[real_name]
    return real_name

def find_max(cards,exception,steps):
    """Find the maximum of the given cards except the cards that have been already picked by hand_value """
    ranks = []
    for rank,suit in cards:
        if rank not in exception:
            ranks.append(rank)
            if len(ranks)==steps:
                return ranks