def first_participation(country, file_address):
    list_of_year = []
    dict_country_years = {country: {}}
    with open(file_address, 'r') as olympics_data:
        next(olympics_data)
        for line in olympics_data:
            list_of_information = line.split("\t")
            year = list_of_information[9]
            city = list_of_information[11]
            if (country in dict_country_years) and year not in dict_country_years[country]:
                dict_country_years[country][year] = city
    for year in dict_country_years[country]:
        year_int = int(year)
        list_of_year.append(year_int)
    min_year = min(list_of_year)
    result = f"The first participation of {country} is {min_year} in {dict_country_years[country][year]}"
    return result