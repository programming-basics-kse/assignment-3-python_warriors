def max_values(dict_country_medals, country):
    max_year = None
    max_medals = 0
    gold_medals = silver_medals = bronze_medals = 0
    for year, medals in dict_country_medals[country].items():
        total_medals = medals["Gold"] + medals["Silver"] + medals["Bronze"]
        if total_medals > max_medals:
            max_medals = total_medals
            max_year = year
            gold_medals = medals["Gold"]
            silver_medals = medals["Silver"]
            bronze_medals = medals["Bronze"]
    result_max = f"{country} - Year with highest numbers of medals: {max_year} ({max_medals} medals)\nGold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals}"
    return result_max



def first_participation(country, file_address):
    list_of_year = []
    dict_country_years = {country: {}}
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            list_of_information = line.split("\t")
            year = list_of_information[9]
            city = list_of_information[11]
            if country in line and year not in dict_country_years[country]:
                dict_country_years[country][year] = city
    for year in dict_country_years[country]:
        year_int = int(year)
        list_of_year.append(year_int)
    min_year = min(list_of_year)
    result = f"The first participation of {country} is {min_year} in {dict_country_years[country][year]}"
    return result


def average_medals(dict_country_medals, country, count_of_sports, list_of_years):
    results = []
    for year in list_of_years:
        if year in dict_country_medals[country]:
            average_gold_medals = dict_country_medals[country][year]["Gold"] / count_of_sports
            average_silver_medals = dict_country_medals[country][year]["Silver"] / count_of_sports
            average_bronze_medals = dict_country_medals[country][year]["Bronze"] / count_of_sports
            result = f"Average in {year}:\n Gold medals: {average_gold_medals}\n Silver medals: {average_silver_medals}\n Bronze medals: {average_bronze_medals}\n"
            results.append(result)
    return results