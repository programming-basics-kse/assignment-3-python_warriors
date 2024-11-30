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

def winners(file_address, number_of_people, output_file, gender, category_filter=None):
    winners = []
    medals = {}
    counter = 0
    with open(file_address, "r") as olympic:
        for line in olympic:
            list_of_information = line.split("\t")
            medal_type = list_of_information[14].strip()
            name = list_of_information[1]
            discipline = list_of_information[12]
            if category_filter is not None:
                weight = int(list_of_information[5])
                age = int(list_of_information[3])
                height = int(list_of_information[4])
            result = f"{name} - {discipline}"
            if (gender is None or gender in line) and medal_type in {"Gold", "Silver", "Bronze"}:
                if category_filter:
                    if name not in medals:
                        medals[name] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                    medals[name][medal_type] += 1
                    if medals[name]["Gold"] > 3 or medals[name]["Silver"] > 3 or medals[name]["Bronze"] > 3:
                        if counter < number_of_people:
                            counter += 1
                            if output_file is not None and counter <= number_of_people:
                                winners.append(result)
                            elif output_file is None and counter <= number_of_people:
                                print(result)



def category(file_address, number_of_people, gender, choice, number_of_choice, output_file):
    pass
