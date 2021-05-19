""" This Module provides all constant variables """

class Constant():
    MAX_PLAYER = 22
    MIN_PLAYER = 1
    
    RANKS = '23456789TJQKA'
    SUITS='SHDC'
    RANKS_LIST = [12,11,10,9,8,7,6,5,4,3,2,1,0]

    MAPPING_RANKS ={
         "T":10 ,
         "J": "Jack",
         "Q": "Queen",
         "K" :"King" ,
         "A" : "Ace"
    }
    
    #  The constants used for mapping the selected 5 cards to a universal score
    #  so each card's rank will divide by corresponding   constant
    RATIOS=[1,10,100,1000,10000]
   
    # Base Score for each hand value
    ROYAL_FLUSH = 900
    STRIGHT_FLUSH = 800
    FOUR_OF_KIND = 700
    FULL_HOUSE = 600
    FLUSH = 500
    STRIGHT = 400
    THREE_OF_KIND = 300
    TWO_PAIR = 200
    PAIR = 100
    HIGH_CARD = 0

    
    