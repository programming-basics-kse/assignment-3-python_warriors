def total_medals(file_address, year_input, output="", result_file=""):
    result ={}
    gold = 0
    silver = 0
    bronze = 0
    with open(file_address, 'r') as olympics_data:
        for line in olympics_data:
            data_list = line.split('\t')
            country = data_list[6]
            year_of_olympic = data_list[10]
            medal_type = data_list[14].strip()
            if year_input == year_of_olympic in line:
                for country in line:
                    if medal_type == "Gold":
                        gold  += 1
                        result[country] = gold
                    elif medal_type == "Silver":
                        silver += 1
                        result[country] = silver
                    elif medal_type == "Bronze":
                        bronze += 1
                        x = input()
                    result[country] = {[gold], [silver], [bronze]}
        for country, medals in result.items():
            print(f"{country} - {medals["gold"]} - {medals["silver"]} - {medals["bronze"]}")


total_medals("OlympicAthletes-athlete_events.tsv", "2000")


