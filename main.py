import argparse


def min_values(dict_country_medals, country):
    min_year = min(dict_country_medals[country],
                   key=lambda year: sum(dict_country_medals[country][year].values()))
    min_medals = sum(dict_country_medals[country][min_year].values())
    gold_medals_min = dict_country_medals[country][min_year]["Gold"]
    silver_medals_min = dict_country_medals[country][min_year]["Silver"]
    bronze_medals_min = dict_country_medals[country][min_year]["Bronze"]
    return min_year, min_medals, gold_medals_min, silver_medals_min, bronze_medals_min


def max_values(dict_country_medals, country):
    max_year = max(dict_country_medals[country],
                   key=lambda year: sum(dict_country_medals[country][year].values()))
    max_medals = sum(dict_country_medals[country][max_year].values())
    gold_medals = dict_country_medals[country][max_year]["Gold"]
    silver_medals = dict_country_medals[country][max_year]["Silver"]
    bronze_medals = dict_country_medals[country][max_year]["Bronze"]
    return max_year, max_medals, gold_medals, silver_medals, bronze_medals


def interactive(country):
    results = []
    list_of_countries = country.split(" ")
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
                max_year, max_medals, gold_medals, silver_medals, bronze_medals= max_values(dict_country_medals,
                                                                                             country)
                min_year, min_medals, gold_medals_min, silver_medals_min, bronze_medals_min = min_values(dict_country_medals,
                                                                                             country)
            except ValueError:
                continue
            result_max = f"{country} - Year with highest numbers of medals: {max_year} ({max_medals} medals)\nGold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals}"
            result_min = f"{country} - Year with highest numbers of medals: {min_year} ({min_medals} medals)\nGold: {gold_medals_min}, Silver: {silver_medals_min}, Bronze: {bronze_medals_min}"
            results.append(result_max)
            results.append(result_min)
            print(result_max +"\n" + result_min)



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
                max_year, max_medals, gold_medals, silver_medals, bronze_medals = max_values(dict_country_medals, country)
            except ValueError:
                continue
            result = f"{country} - Year with highest numbers of medals: {max_year} ({max_medals} medals)\nGold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals}"
            results.append(result)
            if text_file is None:
                print(result)
    if text_file is not None:
        with open(text_file, "w") as result_file:
            for i, result in enumerate(results):
                result_file.write(result + "\n")
        output_from_file(text_file)


def output_from_file(text_file):
    with open(text_file, 'r') as result:
        for line in result:
            print(line)


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
                    if text_file is not None:
                        results.append(result)
                    elif text_file is None and counter < 10:
                        print(result)
    if text_file is None:
        for medal, count in dict_medals.items():
            print(f"{medal} - {count}\n")
    else:
        with open(text_file, "w") as result_file:
            for i, result in enumerate(results):
                if i < 10:
                    result_file.write(result + "\n")
            for medal, count in dict_medals.items():
                result_file.write(f"{medal} - {count}\n")
        output_from_file(text_file)


def total_medals(file_address, year_input, result_file):
    results = []
    dict_for_medals = {}
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            data_list = line.split('\t')
            country = data_list[7]
            year_of_olympic = data_list[9]
            medal_type = data_list[14].strip()
            if year_input == year_of_olympic:
                if country not in dict_for_medals:
                    dict_for_medals[country] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                if medal_type == "Gold":
                    dict_for_medals[country][medal_type] += 1
                elif medal_type == "Silver":
                    dict_for_medals[country][medal_type] += 1
                elif medal_type == "Bronze":
                    dict_for_medals[country][medal_type] += 1
        for country, medals in dict_for_medals.items():
            result = f"{country} - Gold medals:{dict_for_medals[country]['Gold']} - Silver medals:{dict_for_medals[country]['Silver']} - Bronze medals:{dict_for_medals[country]['Bronze']}"
            if result_file is None:
                print(result)
            else:
                results.append(result)
        if result_file is not None:
            with open(result_file, "w") as file:
                for result in results:
                    file.write(result + "\n")
            output_from_file(result_file)


parser = argparse.ArgumentParser("Information from user about olympic data")
parser.add_argument("address_file", type=str, help="File with data")
parser.add_argument("command", choices=["medals", "total", "overall", "interactive"], help="optional")
parser.add_argument("arg", nargs="*", help="")
parser.add_argument("-output", type=str, help="Output file", default=None)

args = parser.parse_args()
file_address = args.address_file
command = args.command
args_for_function = args.arg
output_file = args.output


if command == "medals":
    country = args_for_function[0]
    year_of_olympics = args_for_function[1]
    output_into_scr(file_address, country, year_of_olympics, output_file)
elif command == "total":
    year_of_olympics = args_for_function[0]
    total_medals(file_address, year_of_olympics, output_file)
elif command == "overall":
    overall(file_address, " ".join(args_for_function), output_file)

