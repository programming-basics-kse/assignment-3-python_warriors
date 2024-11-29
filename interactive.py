import auxiliary_function
import first_participation
import work_with_file
def interactive(file_address, country, text_file):
    varification = 0
    count_of_sports = 0
    list_of_years = []
    results = []
    dict_country_medals = {country: {}}
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            list_of_information = line.split("\t")
            year = list_of_information[9]
            medal_type = list_of_information[14].strip()
            if year not in list_of_years:
                list_of_years.append(year)
            for country in dict_country_medals:
                if country in line:
                    varification += 1
                    if year not in dict_country_medals[country]:
                        count_of_sports += 1
                        dict_country_medals[country][year] = {"Gold": 0, "Silver": 0, "Bronze": 0, "NA": 0}
                    dict_country_medals[country][year][medal_type] += 1
    if varification != 0 and count_of_sports != 0:
        result_max = auxiliary_function.max_min_values(dict_country_medals, country, "max")
        result_min = auxiliary_function.max_min_values(dict_country_medals, country,"min")
        results_average = auxiliary_function.average_medals(dict_country_medals, country, count_of_sports, list_of_years)
        results.append(result_max)
        results.append(result_min)
        for res in results_average:
            results.append(res)
        if text_file is None:
            for res in results_average:
                print(res)
            print(result_max)
            print(result_min)
        first_country = first_participation.first_participation(country, file_address)
        print(first_country)
        results.append(first_country)
    else:
        if text_file is None:
            print("No such country")
        else:
            results.append("No such country")
    if text_file is not None:
        work_with_file.write_result_into_file(text_file, results)
        work_with_file.output_from_file(text_file)