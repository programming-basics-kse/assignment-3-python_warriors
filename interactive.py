import work_with_file as wf
import additional_function as af
def interactive(file_address, country, text_file):
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
                    if year not in dict_country_medals[country]:
                        count_of_sports += 1
                        dict_country_medals[country][year] = {"Gold": 0, "Silver": 0, "Bronze": 0, "NA": 0}
                    dict_country_medals[country][year][medal_type] += 1
    result_max = af.max_values(dict_country_medals, country)
    results_average = af.average_medals(dict_country_medals, country, count_of_sports, list_of_years)
    results.append(result_max)
    for res in results_average:
        results.append(res)
    if text_file is None:
        for res in results_average:
            print(res)
        print(result_max)
    first_country = af.first_participation(country, file_address)
    print(first_country)
    results.append(first_country)
    if text_file is not None:
        wf.write_result_into_file(text_file, results)
        wf.output_from_file(text_file)