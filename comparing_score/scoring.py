

def display_result(result):
    initial_sorting_based_on_score =sorted(result,key=lambda x:x['score'])
    # check if we need to active the kickers
    add_kickers_to_result=check_to_Show_kickers(initial_sorting_based_on_score)
    # sorting result
    sorted_result=sorting_result(add_kickers_to_result)
    # display
    display(sorted_result)




def sorting_result(results):
    """ Based on scores, creatign a dictioanry where key is score and then sorting by key"""
    result_dict={}
    for result in results:
        result_dict[result['score']]= result_dict.get(result['score'], [])+[result ] 
    sorted_result=[]
    for i in sorted (result_dict.keys(),reverse=True): 
        sorted_result.append(result_dict[i])
    return sorted_result



def display(sorted_result):
    """ Display result to console"""
    for i in range(len(sorted_result)):
        final_name=""
        hand_value= sorted_result[i][0]['hand_value']
        
        for player in sorted_result[i]:

            name=player['name']
            final_name+=name+" "
        
        kickers=None
        kickers = check_kickers(sorted_result[i])
        if   kickers:
            print(f'{i+1} {final_name}  {hand_value}, Kickers {kickers}')
        else:
            print(f'{i+1} {final_name}  {hand_value}')

def check_to_Show_kickers(result):
    """ Add a new property (active_kickers) to player by evaluating the score and hand value"""
    for player_one,player_two in zip(result,result[1:]):
        if player_one['score'] != player_two['score'] and player_one['hand_value'] == player_two['hand_value']:
           player_one['active_kickers']=True
           player_two['active_kickers']=True
    return result

def check_kickers(cards):
    """ Return Kickers if the kicker is active"""
    for card in cards:
        if  "active_kickers" in  card and 'kickers' in card:
            return card['kickers']
    return False

