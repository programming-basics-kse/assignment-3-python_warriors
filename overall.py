import work_with_file as wf
import additional_function as af

def overall(file_address, countries, text_file):
    results = []
    list_of_countries = countries.split(" ")
    dict_country_medals = {country: {} for country in list_of_countries}
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            list_of_information = line.split("\t")
            year = list_of_information[9]
            medal_type = list_of_information[14].strip()
            for country in list_of_countries:
                if country in line and medal_type in {"Gold", "Silver", "Bronze"}:
                    if year not in dict_country_medals[country]:
                        dict_country_medals[country][year] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                    dict_country_medals[country][year][medal_type] += 1
    for country in list_of_countries:
        if country in dict_country_medals and dict_country_medals[country]:
            try:
                results_max = af.max_values(dict_country_medals, country)
            except ValueError:
                continue
            results.append(results_max)
            if text_file is None:
                print(results_max)
    if text_file is not None:
        wf.write_result_into_file(text_file, results)
        wf.output_from_file(text_file)

