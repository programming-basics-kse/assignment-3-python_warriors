def output_from_file(text_file):
    with open(text_file, 'r') as result:
        for line in result:
            print(line)


def output_into_scr(file_address, medals, country, year_of_olympics, output="", text_file=""):
    dict_medals = {}
    results = []
    counter = 0
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            if (country in line) and (year_of_olympics in line):
                counter += 1
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


output_into_scr("OlympicAthletes-athlete_events.tsv", "-medals", "USA", "1976", "-output", "result.txt")

while True:
    user_information = input("Enter your data:\n")
    data = user_information.split(" ")
    if len(data) >= 5:
        file_address = data[1]
        medals = data[2]
        country = data[3]
        year_of_olympic = data[4]
        if len(data) == 7:
            output = data[5]
            result_output = data[6]
            output_into_scr(file_address, medals, country, year_of_olympic, output, result_output)
        else:
            output_into_scr(file_address, medals, country, year_of_olympic)
    else:
        print("Invalid input, please try again")
