import argparse

def overall(file_address, countries, output="", text_file=""):
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
                max_year = max(dict_country_medals[country], key=lambda year: sum(dict_country_medals[country][year].values()))
                max_medals = sum(dict_country_medals[country][max_year].values())
            except ValueError:
                continue
            gold_medals = dict_country_medals[country][max_year]["Gold"]
            silver_medals = dict_country_medals[country][max_year]["Silver"]
            bronze_medals = dict_country_medals[country][max_year]["Bronze"]
            result = f"{country} - Year with most medals: {max_year} ({max_medals} medals)\nGold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals}"
            results.append(result)
            if output != "-output":
                print(result)
    if output == "-output":
        with open(text_file, "w") as result_file:
            for i, result in enumerate(results):
                result_file.write(result + "\n")
        output_from_file(text_file)


def output_from_file(text_file):
    with open(text_file, 'r') as result:
        for line in result:
            print(line)


def output_into_scr(file_address, country, year_of_olympics, output="", text_file=""):
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
                    if output == "-output":
                        results.append(result)
                    elif output != "-output" and counter < 10:
                        print(result)
    if output != "-output":
        for medal, count in dict_medals.items():
            print(f"{medal} - {count}\n")
    if output == "-output":
        with open(text_file, "w") as result_file:
            for i, result in enumerate(results):
                if i <= 10:
                    result_file.write(result + "\n")
            for medal, count in dict_medals.items():
                result_file.write(f"{medal} - {count}\n")
        output_from_file(text_file)


def total_medals(file_address, total, year_input, output="", result_file=""):
    result ={}
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            if "total" in total:
                data_list = line.split('\t')
                country = data_list[6]
                year_of_olympic = data_list[10]
                medal_type = data_list[14].strip()
                if year_input == year_of_olympic and year_of_olympic in line:
                    if medal_type != "NA":
                        if country not in result:
                            result[country] = medal_type
                        elif country in result:
                            result[country] += medal_type
    if output != "output":
        for country, medal_type in result.items():
            print(f"{country} - {medal_type}\n")
    if output == "output":
        with open(result_file, "w") as file:
            for i, result in enumerate(result):
                file.write(result + "\n")
            for country, medal in result.items():
                result_file.write(f"{country} - {medal_type}\n")


parser = argparse.ArgumentParser("Information from user about olympic data")
parser.add_argument("address_file", type=str, help="File with data")
parser.add_argument("command", choices=["medals", "total", "overall"], help="optional")
parser.add_argument("arg", nargs="*", help="")

args = parser.parse_args()
file_address = args.address_file
command = args.command
args_for_function = args.arg

output_file = args_for_function[-1]
output = args_for_function[-2]

if command == "medals":
    country = args_for_function[0]
    year_of_olympics = args_for_function[1]
    if len(args_for_function) == 3:
        output_into_scr(file_address, country, year_of_olympics, output, output_file)
    else:
        output_into_scr(file_address, country, year_of_olympics)
elif command == "total":
    year_of_olympics = args_for_function[0]
    if len(args_for_function) == 2:
        total_medals(file_address, command, year_of_olympics, output, output_file)
    else:
        total_medals(file_address, command, year_of_olympics)
elif command == "overall":
    country = args_for_function[:-1]
    if args_for_function[-2] == "-output" or args_for_function[-2] == "output":
        overall(file_address, " ".join(country), output, output_file)
    else:
        overall(file_address, " ".join(country))
