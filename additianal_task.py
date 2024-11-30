import additional_function as af
def additional_task(file_address, list_of_data, output_file):
    if len(list_of_data) == 1:
        number_of_people = list_of_data[0]
        winners(file_address, number_of_people, output_file, gender=None)
    if len(list_of_data) == 2:
        number_of_people = list_of_data[0]
        gender = list_of_data[1]
        winners(file_address, number_of_people, output_file, gender)
    if len(list_of_data) == 4:
        number_of_people = list_of_data[0]
        gender = list_of_data[1]
        choice = list_of_data[2]
        number_of_choice = list_of_data[3]
        category(file_address, number_of_people, gender, choice, number_of_choice, output_file)

def winners(file_address, number_of_people, output_file, gender):
    pass


def category(file_address, number_of_people, gender, choice, number_of_choice, output_file):
    pass
