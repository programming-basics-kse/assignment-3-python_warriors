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
