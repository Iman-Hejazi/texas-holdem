
from poker_texas_holdem.evaluating_hand import evaluating_hand


def evaluation(players):
    results=[]
    for player in players:
        result = evaluating_hand(player['hand'])
        result['name']=player['name']
        results.append(result)
    return results