import Analysis
import Database

# Database.import_data("./data/data.csv")
# Database.create_backup()

is_in_main_menu = True

while is_in_main_menu:
    input_string = input("1.Get new cases information\n2.Get deaths information\n3.Exit\n")
    if input_string == "1":
        print("New Cases Menu")
        is_in_cases_menu = True
        while is_in_cases_menu:
            cases_input = input("1.Get plot of median new cases in 2020 in certain country\n" 
                        "2.Get plot of average new cases in 2020 in certain country\n" 
                        "3.Get tendency of new cases in 2020 in certain country\n" 
                        "4.Get complete statistic of new cases in 2020 in certain country\n" 
                        "5.Get comparison of new cases tendency in different countries in certain interval\n"
                        "6.Get all cases cumulative in certain interval\n" 
                        "7.Exit to Main Menu\n")
            if cases_input == "1":
                country_input = input("Enter country:\n")
                Analysis.get_cases_median_by_country(country_input)
            elif cases_input == "2":
                country_input = input("Enter country:\n")
                Analysis.get_cases_average_by_country(country_input)
            elif cases_input == "3":
                country_input = input("Enter country:\n")
                Analysis.get_cases_tendency_by_country(country_input)
            elif cases_input == "4":
                country_input = input("Enter country:\n")
                Analysis.get_cases_complete_by_country(country_input)
            elif cases_input == "5":
                interval_start = input("Enter start of interval:\n")
                interval_end = input("Enter end of interval:\n")
                Analysis.get_cases_tendency_in_period(interval_start, interval_end)
            elif cases_input == "6":
                interval_start = input("Enter start of interval:\n")
                interval_end = input("Enter end of interval:\n")
                Analysis.get_cases_cumulative_in_period(interval_start, interval_end)
            elif cases_input == "7":
                is_in_cases_menu = False
            else:
                print("Choose one of available options")
    elif input_string == "2":
        print("Deaths menu")
        is_in_deaths_menu = True
        while is_in_deaths_menu:
            deaths_input = input("1.Get plot of median deaths in 2020 in certain country\n"
                                "2.Get plot of average deaths in 2020 in certain country\n"
                                "3.Get tendency of deaths in 2020 in certain country\n"
                                "4.Get complete statistic of deaths in 2020 in certain country\n"
                                "5.Get comparison of deaths tendency in different countries in certain interval\n"
                                "6.Get all deaths cumulative in period\n"
                                "7.Exit to Main Menu\n")
            if deaths_input == "1":
                country_input = input("Enter country:\n")
                Analysis.get_deaths_median_by_country(country_input)
            elif deaths_input == "2":
                country_input = input("Enter country:\n")
                Analysis.get_deaths_average_by_country(country_input)
            elif deaths_input == "3":
                country_input = input("Enter country:\n")
                Analysis.get_deaths_tendency_by_country(country_input)
            elif deaths_input == "4":
                country_input = input("Enter country:\n")
                Analysis.get_deaths_complete_by_country(country_input)
            elif deaths_input == "5":
                interval_start = input("Enter start of interval:\n")
                interval_end = input("Enter end of interval:\n")
                Analysis.get_deaths_tendency_in_period(interval_start, interval_end)
            elif deaths_input == "6":
                interval_start = input("Enter start of interval:\n")
                interval_end = input("Enter end of interval:\n")
                Analysis.get_deaths_cumulative_in_period(interval_start, interval_end)
            elif deaths_input == "7":
                is_in_deaths_menu = False
            else:
                print("Choose one of available options")
    elif input_string == "3":
        print("Goodbye")
        is_in_main_menu = False
    else:
        print("Choose one of available options")

