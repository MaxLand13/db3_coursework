import pandas as pd
import matplotlib.pyplot as plt
import Database
from datetime import timedelta


def get_cases_median_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.cases != 0]
    fig, ax = plt.subplots()
    ax.plot(dataframe['dateRep'], dataframe['cases'], label='Cases')
    title = "Median in " + str(country) + " is " + str(dataframe['cases'].median()) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index)*0.2, len(dataframe.index)*0.4, len(dataframe.index)*0.6, len(dataframe.index)*0.8, len(dataframe.index) - 1])
    plt.axhline(y=dataframe['cases'].median(), color='r', linestyle='--', alpha=0.5, label='Median')
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_median_cases.png"
    plt.savefig(filepath)
    plt.show()


def get_cases_average_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.cases != 0]
    fig, ax = plt.subplots()
    ax.plot(dataframe['dateRep'], dataframe['cases'], label='Cases')
    title = "Average in " + str(country) + " is " + str(dataframe['cases'].mean()) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(y=dataframe['cases'].mean(), color='r', linestyle='--', alpha=0.5, label='Average')
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_average_cases.png"
    plt.savefig(filepath)
    plt.show()


def get_cases_tendency_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.cases != 0]
    fig, ax = plt.subplots()
    difference = dataframe['cases'].diff(periods=7)
    difference = difference.fillna(0)

    ax.plot(dataframe['dateRep'], difference, label='Tendency')
    title = "Average tendency " + str(country) + " is " + str(difference.mean()) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(0, color='r', linestyle='-', label='Zero tendency', alpha=0.75)
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_tendency_cases.png"
    plt.savefig(filepath)
    plt.show()


def get_cases_complete_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.cases != 0]
    fig, ax = plt.subplots()
    ax.plot(dataframe['dateRep'], dataframe['cases'], label='Cases')
    title = "Complete statistic in " + str(country) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(y=dataframe['cases'].median(), color='r', linestyle='--', alpha=0.5, label='Median is ' + str(dataframe['cases'].median()))
    plt.axhline(y=dataframe['cases'].mean(), color='g', linestyle='--', alpha=0.5, label='Average is ' + str(dataframe['cases'].mean()))

    difference = dataframe['cases'].diff(periods=7)
    difference = difference.fillna(0)

    ax.plot(dataframe['dateRep'], difference, label='Tendency')
    plt.axhline(0, color='b', linestyle='-', label='Zero tendency', alpha=0.75)
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_complete_cases.png"
    plt.savefig(filepath)
    plt.show()


def get_deaths_median_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.deaths != 0]
    fig, ax = plt.subplots()
    ax.plot(dataframe['dateRep'], dataframe['deaths'], label='Deaths')
    title = "Median deaths in " + str(country) + " is " + str(dataframe['deaths'].median()) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(y=dataframe['deaths'].median(), color='r', linestyle='--', alpha=0.5, label='Median deaths')
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_median_deaths.png"
    plt.savefig(filepath)
    plt.show()


def get_deaths_average_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.deaths != 0]
    fig, ax = plt.subplots()
    ax.plot(dataframe['dateRep'], dataframe['deaths'], label='Deaths')
    title = "Average deaths in " + str(country) + " is " + str(dataframe['deaths'].mean()) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(y=dataframe['deaths'].mean(), color='r', linestyle='--', alpha=0.5, label='Average deaths')
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_average_deaths.png"
    plt.savefig(filepath)
    plt.show()


def get_deaths_tendency_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.deaths != 0]
    fig, ax = plt.subplots()
    difference = dataframe['deaths'].diff(periods=7)
    difference = difference.fillna(0)

    ax.plot(dataframe['dateRep'], difference, label='Death tendency')
    title = "Average deaths tendency " + str(country) + " is " + str(difference.mean()) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(0, color='r', linestyle='-', label='Zero death tendency', alpha=0.75)
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_tendency_deaths.png"
    plt.savefig(filepath)
    plt.show()


def get_deaths_complete_by_country(country):
    country = process_country(country)
    dataframe = Database.get_by_filter({"countriesAndTerritories": country})
    if dataframe.empty:
        return print("Invalid Country name")
    dataframe = dataframe[dataframe.deaths != 0]
    fig, ax = plt.subplots()
    ax.plot(dataframe['dateRep'], dataframe['deaths'], label='Deaths')
    title = "Complete deaths statistic in " + str(country) + " in 2020"
    ax.set_title(title)
    ax.invert_xaxis()
    ax.set_xticks([0, len(dataframe.index) * 0.2, len(dataframe.index) * 0.4, len(dataframe.index) * 0.6,
                   len(dataframe.index) * 0.8, len(dataframe.index) - 1])
    plt.axhline(y=dataframe['deaths'].median(), color='r', linestyle='--', alpha=0.5,
                label='Median deaths is ' + str(dataframe['deaths'].median()))
    plt.axhline(y=dataframe['deaths'].mean(), color='g', linestyle='--', alpha=0.5,
                label='Average deaths is ' + str(dataframe['deaths'].mean()))

    difference = dataframe['deaths'].diff(periods=7)
    difference = difference.fillna(0)

    ax.plot(dataframe['dateRep'], difference, label='Deaths tendency')
    plt.axhline(0, color='b', linestyle='-', label='Zero deaths tendency', alpha=0.75)
    ax.legend(loc="upper left")
    filepath = "./results/" + str(country) + "_complete_deaths.png"
    plt.savefig(filepath)
    plt.show()


def get_cases_tendency_in_period(start_date, end_date):
    try:
        dates = pd.date_range(start=start_date, end=end_date).strftime("%d/%m/%Y").to_list()
    except BaseException:
        return print("Invalid Interval Format, please write in next format 'day-month-year'\n\n")

    query = []
    for date in dates:
        query.append({"dateRep":str(date)})
    dataframe = Database.get_by_filter({"$or": query})
    dataframe = dataframe.groupby('countriesAndTerritories')[['countriesAndTerritories', 'cases']].sum()
    if dataframe.empty:
        return print("Invalid Interval")
    dataframe = dataframe.sort_values(by=['cases'])
    best = dataframe.head(10)
    worst = dataframe.tail(10).sort_values(by=['cases'], ascending=False)
    print("\n\nBest countries by tendency of new cases in period:")
    print(best)
    print("\n\nWorst countries by tendency of new cases in period:")
    print(worst)


def get_deaths_tendency_in_period(start_date, end_date):
    try:
        dates = pd.date_range(start=start_date, end=end_date).strftime("%d/%m/%Y").to_list()
    except BaseException:
        return print("Invalid Interval Format, please write in next format 'day-month-year'\n\n")
    query = []
    for date in dates:
        query.append({"dateRep":str(date)})
    dataframe = Database.get_by_filter({"$or": query})
    dataframe = dataframe.groupby('countriesAndTerritories')[['countriesAndTerritories','deaths']].sum()
    if dataframe.empty:
        return print("Invalid Interval")
    dataframe = dataframe.sort_values(by=['deaths'])
    best = dataframe.head(10)
    worst = dataframe.tail(10).sort_values(by=['deaths'], ascending=False)
    print("\n\nBest countries by tendency of deaths in period:")
    print(best)
    print("\n\nWorst countries by tendency of deaths in period:")
    print(worst)


def get_cases_cumulative_in_period(start_date, end_date):
    try:
        dates = pd.date_range(start=start_date, end=end_date).strftime("%d/%m/%Y").to_list()
    except BaseException:
        return print("Invalid Interval Format, please write in next format 'day-month-year'\n\n")

    query = []
    for date in dates:
        query.append({"dateRep":str(date)})
    dataframe = Database.get_by_filter({"$or": query})
    dataframe = dataframe.groupby('dateRep')[['dateRep', 'cases']].sum()
    if dataframe.empty:
        return print("Invalid Interval")
    dataframe['cases'] = dataframe['cases'].cumsum()
    worst = dataframe.tail(10).sort_values(by=['cases'], ascending=False)
    print("\n\nGrowth of new cases in period:")
    print(worst)


def get_deaths_cumulative_in_period(start_date, end_date):
    try:
        dates = pd.date_range(start=start_date, end=end_date).strftime("%d/%m/%Y").to_list()
    except BaseException:
        return print("Invalid Interval Format, please write in next format 'day-month-year'\n\n")

    query = []
    for date in dates:
        query.append({"dateRep":str(date)})
    dataframe = Database.get_by_filter({"$or": query})
    dataframe = dataframe.groupby('dateRep')[['dateRep', 'deaths']].sum()
    if dataframe.empty:
        return print("Invalid Interval")
    dataframe['deaths'] = dataframe['deaths'].cumsum()
    worst = dataframe.tail(10).sort_values(by=['deaths'], ascending=False)
    print("\n\nDeaths in period:")
    print(worst)


def process_country(country):
    country = country.rstrip()
    country = country.lstrip()
    country = ' '.join(country.split())
    country = country.replace(" ", "_")
    return country
