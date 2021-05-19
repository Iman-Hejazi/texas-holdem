from preparing_data.data_validaiton import timming_lines,checking_numbers_of_lines



def reading_data_from_file(file_name):
    trimmed_lines=[]
    with open(file_name) as fp:
        lines = fp.readlines()
        trimmed_lines=timming_lines(lines)
        checking_numbers_of_lines(len(trimmed_lines))   
    return trimmed_lines   




def preparing_file_name(name_of_file):
    name_of_file=name_of_file.strip()
    file_name=""
    if name_of_file=="":
        print("Result form cards.txt which is a sample")
        file_name = 'cards.txt'
    else:
        file_name= name_of_file +".txt"
    return file_name