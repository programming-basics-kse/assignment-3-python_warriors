import argparse

parser = argparse.ArgumentParser("Information from user about olympic data")

parser.add_argument("address_file", help="File with data")
parser.add_argument("medals")
parser.add_argument("total", help="optional")
parser.add_argument("overall",  help="optional")
parser.add_argument("country", nargs="*")
parser.add_argument("year")
parser.add_argument("output",  help="optional")
parser.add_argument("result_file",  help="optional")

args = parser.parse_args()


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



# total_medals(args.address_file, args.total, args.year)


