def max_min_values(dict_country_medals, country, max_or_min):
    min_max_year = None
    max_medals = 0
    min_medals = float('inf')
    gold_medals = silver_medals = bronze_medals = 0
    for year, medals in dict_country_medals[country].items():
        total_medals = medals["Gold"] + medals["Silver"] + medals["Bronze"]
        if max_or_min == "min":
            if total_medals < min_medals:
                min_medals = total_medals
                min_max_year = year
                gold_medals = medals["Gold"]
                silver_medals = medals["Silver"]
                bronze_medals = medals["Bronze"]
        elif max_or_min == "max":
            if total_medals > max_medals:
                max_medals = total_medals
                min_max_year = year
                gold_medals = medals["Gold"]
                silver_medals = medals["Silver"]
                bronze_medals = medals["Bronze"]
    if max_or_min == "min":
        result = f"{country} - Year with lowest numbers of medals: {min_max_year} ({min_medals} medals)\nGold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals}"
    elif max_or_min == "max":
        result = f"{country} - Year with highest numbers of medals: {min_max_year} ({max_medals} medals)\nGold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals}"
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