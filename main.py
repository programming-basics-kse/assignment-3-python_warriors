def output_into_scr(file_address, medals, country, year_of_olympics, output, text_file):
    if output == "-output":
        output_file = open(text_file, 'w')
    gold_medals = 0
    silver_medals = 0
    bronze_medals = 0
    counter = 0
    counter_for_file = 0
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            if (country in line) and (year_of_olympics in line):
                counter += 1
                list_of_information = line.split("\t")
                name = list_of_information[1]
                discipline = list_of_information[12]
                medal_type = list_of_information[14]
                if medal_type == "Gold":
                    gold_medals += 1
                elif medal_type == "Silver":
                    silver_medals += 1
                elif medal_type == "Bronze":
                    bronze_medals += 1
                if output == "-output":
                    output_file.write(f"{name} - {discipline} - {medal_type}")
                if counter < 10:
                    if output != "-output":
                        print(f"{name} - {discipline} - {medal_type}")
    if output != "-output":
        print(f"Gold - {gold_medals}\nSilver - {silver_medals}\nBronze - {bronze_medals}")
    if output == "-output":
        output_file.close()
        with open(text_file, 'r') as result:
            for line in result:
                counter_for_file += 1
                if counter_for_file <= 10:
                    print(line)
                elif counter_for_file == 11:
                    output_file.write(f"Gold - {gold_medals}\nSilver - {silver_medals}\nBronze - {bronze_medals}")


def user_input():
    while True:
        user_information = input("Enter your data:\n")
        data = user_information.split(" ")
        if len(data) == 5:
            file_address = data[1]
            medals = data[2]
            country = data[3]
            year_of_olympic = data[4]
            return file_address, medals, country, year_of_olympic
        elif len(data) == 7:
            file_address = data[1]
            medals = data[2]
            country = data[3]
            year_of_olympic = data[4]
            output = data[5]
            result_output = data[6]
            return file_address, medals, country, year_of_olympic, output, result_output
        else:
            print("Invalid input, please try again")


output_into_scr("Olympic Athletes - athlete_events.tsv", "-medals", "AUT", "1976", "-output", "result.txt")