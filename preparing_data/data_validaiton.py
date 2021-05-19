from custom_exception.custom_exception import CustomError
from constant import Constant as CONST



def timming_lines(lines):
    non_empty_lines = [line for line in lines if line.strip() != ""]
    return [line.strip() for line in non_empty_lines]




def checking_numbers_of_lines(nums):
    if nums==0:
        raise CustomError ("File must have community Cards and at least one player's hand")
    if nums==CONST.MIN_PLAYER:
        raise CustomError ("File must have at least one player's hand")   
    if nums >= CONST.MAX_PLAYER+1:
        raise CustomError (f'The maximum number of players for evaluation must be less than {CONST.MAX_PLAYER}') 