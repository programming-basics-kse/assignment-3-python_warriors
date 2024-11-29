import work_with_file
def output_into_scr(file_address, country, year_of_olympics, text_file):
    dict_medals = {}
    results = []
    counter = 0
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            if (country in line) and (year_of_olympics in line):
                list_of_information = line.split("\t")
                name = list_of_information[1]
                discipline = list_of_information[12]
                medal_type = list_of_information[14].strip()
                result = f"{name} - {discipline} - {medal_type}"
                if medal_type in dict_medals:
                    dict_medals[medal_type] += 1
                else:
                    dict_medals[medal_type] = 1
                if (medal_type == "Bronze") or (medal_type == "Silver") or (medal_type == "Gold"):
                    counter += 1
                    if text_file is not None and counter <= 10:
                        results.append(result)
                    elif text_file is None and counter <= 10:
                        print(result)
    if counter == 0:
        if text_file is None:
            print("There were no winners this year.")
        results.append("There were no winners this year.")
    for medal, count in dict_medals.items():
        number_of_medals = f"{medal} - {count}\n"
        results.append(number_of_medals)
        if text_file is None:
            print(number_of_medals)
    if text_file is not None:
        work_with_file.write_result_into_file(text_file, results)
        work_with_file.output_from_file(text_file)