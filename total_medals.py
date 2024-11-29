import work_with_file

def total_medals(file_address, year_input, result_file):
    results = []
    dict_for_medals = {}
    verification = 0
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            data_list = line.split('\t')
            country = data_list[7].strip()
            year_of_olympic = data_list[9]
            medal_type = data_list[14].strip()
            if year_input == year_of_olympic:
                if country not in dict_for_medals:
                    dict_for_medals[country] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                if medal_type in dict_for_medals[country]:
                    dict_for_medals[country][medal_type] += 1
    for country in dict_for_medals:
        if (dict_for_medals[country]['Gold'] > 1) or (dict_for_medals[country]['Silver'] > 1) or (
                dict_for_medals[country]['Bronze'] > 1):
            verification += 1
            result = f"{country} - Gold medals:{dict_for_medals[country]['Gold']} - Silver medals:{dict_for_medals[country]['Silver']} - Bronze medals:{dict_for_medals[country]['Bronze']}"
            if result_file is None:
                print(result)
            else:
                results.append(result)
    if verification == 0:
        if result_file is None:
            print("There was no Olympics this year")
        results.append("There was no Olympics this year")
    if result_file is not None:
        work_with_file.write_result_into_file(result_file, results)
        work_with_file.output_from_file(result_file)