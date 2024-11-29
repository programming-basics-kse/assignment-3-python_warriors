import argparse
import sys

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


def first_participation(country):
    list_of_year = []
    dict_country_years = {country: {}}
    with open("OlympicAthletes-athlete_events.tsv", 'r') as olympics_data:
        next(olympics_data)
        for line in olympics_data:
            list_of_information = line.split("\t")
            year = list_of_information[9]
            city = list_of_information[11]
            if (country in dict_country_years) and year not in dict_country_years[country]:
                dict_country_years[country][year] = city
    print(dict_country_years)
    for year in dict_country_years[country]:
        year_int = int(year)
        list_of_year.append(year_int)
    min_year = min(list_of_year)
    result = f"The first participation of {country} is {min_year} in {dict_country_years[country][year]}"
    print(result)


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


def write_result_into_file(result_file, results):
    with open(result_file, "w") as file:
        for i, result in enumerate(results):
            file.write(result + "\n")


def output_from_file(text_file):
    with open(text_file, 'r') as result:
        for line in result:
            print(line)

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
    result_max = max_values(dict_country_medals, country)
    results_average = average_medals(dict_country_medals, country, count_of_sports, list_of_years)
    results.append(result_max)
    for res in results_average:
        results.append(res)
    if text_file is None:
        for res in results_average:
            print(res)
        print(result_max)
    first_country = first_participation(country)
    print(first_country)
    results.append(first_country)
    if text_file is not None:
        write_result_into_file(text_file, results)
        output_from_file(text_file)



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
                results_max = max_values(dict_country_medals, country)
            except ValueError:
                continue
            results.append(results_max)
            if text_file is None:
                print(results_max)
    if text_file is not None:
        write_result_into_file(text_file, results)
        output_from_file(text_file)


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
    for medal, count in dict_medals.items():
        number_of_medals = f"{medal} - {count}\n"
        results.append(number_of_medals)
        if text_file is None:
            print(number_of_medals)
    if text_file is not None:
        write_result_into_file(text_file, results)
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
                if medal_type in dict_for_medals[country]:
                    dict_for_medals[country][medal_type] += 1
        for country, medals in dict_for_medals.items():
            if (dict_for_medals[country]['Gold'] > 1) or (dict_for_medals[country]['Silver'] > 1) or (
                    dict_for_medals[country]['Bronze'] > 1):
                result = f"{country} - Gold medals:{dict_for_medals[country]['Gold']} - Silver medals:{dict_for_medals[country]['Silver']} - Bronze medals:{dict_for_medals[country]['Bronze']}"
            if result_file is None:
                print(result)
            else:
                results.append(result)
        if result_file is not None:
            write_result_into_file(result_file, results)
            output_from_file(result_file)


parser = argparse.ArgumentParser("Information from user about olympic data")
parser.add_argument("address_file", type=str, help="File with data")
parser.add_argument("command", choices=["medals", "total", "overall", "interactive"], help="optional")
parser.add_argument("arg", nargs="*", help="")
parser.add_argument("-output", type=str, help="Output file", default=None)

args = parser.parse_args()
file_address = args.address_file
if file_address != "OlympicAthletes-athlete_events.tsv":
    sys.exit()
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
elif command == "interactive":
    country = input("Please enter a country: ")
    interactive(file_address, country, output_file)