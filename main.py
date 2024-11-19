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