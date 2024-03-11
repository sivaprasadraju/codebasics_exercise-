country_population = {
    'China': 143,
    'India': 136,
    'USA': 32,
    'Pakistan': 21
}

def print_dict(dict_data):
    for country in dict_data:
        print(country +"==>"+str(dict_data[country])+"\n")

def add_data_to_dict(dict_data, country):
    print("please enter the population")
    new_population = float(input())
    dict_data.update({country:new_population})
    return dict_data

def main():
    print("Please enter command you want to perform (print, add, remove, query): ")
    user_input = str(input())

    if user_input == "print":
        print_dict(country_population)
    elif user_input == "add":
        print("Please enter the name you want to add: ")
        new_country = str(input())
        if new_country in country_population.keys():
            print("The country which you provided is already exist")
        else:
            new_dict = add_data_to_dict(country_population, new_country)
            print_dict(new_dict)
    elif user_input == "remove":
        print("which country you want to remove from the country_population dictionary: ")
        remove_country = str(input())
        if remove_country in country_population.keys():
            country_population.pop(remove_country)
            print_dict(country_population)
        else:
            print("country doesn't exist")
    elif user_input == "query":
        print("which country you want to query: ")
        query_country = str(input())
        if query_country in country_population.keys():
            print(country_population[query_country])
        else:
            print("Country doesn't exist")

if __name__ == '__main__':
    main()

