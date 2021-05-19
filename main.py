from preparing_data.reading_data_from_consol import reading_data_from_consol
from poker_texas_holdem.main import evaluation
from comparing_score.scoring import display_result
from custom_exception.custom_exception import CustomError




def main():
    try:
        start_evaluation,players = reading_data_from_consol()
        if start_evaluation:
            print("\nStart Evaluation...")
            print("Result:")
            results =evaluation(players)
            display_result(results) 
        else:
            print('Exit')    
    except CustomError as e:
        print(e)
    except Exception:
        print("Internal Server Error")



        

if __name__=="__main__":      
    main()