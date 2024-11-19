def output_into_scr(file_address, medals, country, year_of_olympics, output, text_file):
    create_file = open(text_file, 'w')
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            if (country in line) and (year_of_olympics in line):
                list_of_information = line.split("\t")
                name = list_of_information[1]
                discipline = list_of_information[12]
                medal_type = list_of_information[14]
                if output != "-output":
                    print(f"{name} - {discipline} - {medal_type}")
                else:
                    with open("create_file", 'a') as output_file:
                        output_file.write(f"{name} - {discipline} - {medal_type}")
    if output == "-output":
        with open("create_file", 'r') as output_file:
            print(output_file.read())


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


user_input()