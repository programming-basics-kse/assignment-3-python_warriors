import work_with_file as wf

def additional_task(file_address, list_of_data, output_file):
    number_of_people = list_of_data[0]
    if len(list_of_data) == 1:
        winners(file_address, number_of_people, output_file, gender=None)
    if len(list_of_data) == 2:
        gender = list_of_data[1]
        winners(file_address, number_of_people, output_file, gender)
    if len(list_of_data) == 4:
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
                try:
                    weight = int(list_of_information[5])
                except ValueError:
                    pass
                try:
                    age = int(list_of_information[3])
                except ValueError:
                    pass
                try:
                    height = int(list_of_information[4])
                except ValueError:
                    pass
            result = f"{name} - {discipline}"
            if (gender is None or gender in line) and medal_type in {"Gold", "Silver", "Bronze"}:
                if category_filter:
                    for key, value in category_filter.items():
                        min_val, max_val = value["min"], value["max"]
                        if not (min_val <= age <= max_val):
                            break
                        if key == "a" and not (min_val <= age <= max_val):
                            break
                        elif key == "w" and not (min_val <= weight <= max_val):
                            break
                        elif key == "h" and not (min_val <= height <= max_val):
                            break
                    else:
                        if name not in medals:
                            medals[name] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                        medals[name][medal_type] += 1
                        if medals[name]["Gold"] > 3 or medals[name]["Silver"] > 3 or medals[name]["Bronze"] > 3:
                            if counter < int(number_of_people):
                                counter += 1
                                if output_file is not None and counter <= int(number_of_people):
                                    winners.append(result)
                                elif output_file is None and counter <= int(number_of_people):
                                    print(result)
                else:
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
    if output_file is not None:
        wf.write_result_into_file(output_file, winners)
        wf.output_from_file(output_file)


def category(file_address, number_of_people, gender, number_of_category, output_file):
    category = {"a": {"1": (18, 25),
                     "2": (25, 35),
                     "3": (35, 50),
                     "4": (50, 100)},
                "w": {"1": (40, 60),
                    "2": (60, 80),
                    "3": (80, 100),
                    "4": (100, 300)},
                "h": {"1": (150, 175),
                   "2": (175, 190),
                    "3": (190, 200),
                   "4": (200, 300)}}
    dict_choice = drop(number_of_category)
    if not dict_choice:
        print("Wrong category")
        winners(file_address, number_of_people, output_file, gender)
    else:
        selected_categories = {}
        for key, value in dict_choice.items():
            if key in category and value in category[key]:
                min_val, max_val = category[key][value]
                selected_categories[key] = {"min": min_val, "max": max_val}
        winners(file_address, number_of_people, output_file, gender, selected_categories)



def drop(number_of_category):
    number_of_category = number_of_category.split(" ")
    if len(number_of_category) == 1:
        return None
    else:
        dict_choice = {}
        list_of_action = ["a", "w", "h"]
        for i in range(0, len(number_of_category), 2):
            key = number_of_category[i]
            value = number_of_category[i + 1]
            if key in list_of_action:
                dict_choice[key] = value
        return dict_choice
