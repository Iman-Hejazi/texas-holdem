from poker_texas_holdem.main import evaluation
from comparing_score.scoring import display_result
from custom_exception.custom_exception import CustomError
from preparing_data.preparing_data import creating_players_hand
from preparing_data.reading_data_from_file import reading_data_from_file,preparing_file_name



def main():
    try:
        name_of_file=input('Please enter name of the file (without extention): ')
        file_name = preparing_file_name(name_of_file)
        trimmed_lines= reading_data_from_file(file_name)
        players=creating_players_hand(trimmed_lines)
        results =evaluation(players)
        display_result(results) 
    except FileNotFoundError:
        print('File does not exist')
    except CustomError as e:
        print(e)
    except Exception:
        print("Internal Server Error")






if __name__=="__main__":      
    main()