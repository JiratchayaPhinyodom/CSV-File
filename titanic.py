import csv

# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_single_embarked_survived(place_embarked, age_threshold, titanic_data):
    """This function its important to check all of condition in this function they want
    the number of survived single women over age_threshold embarked at place_embarked
    (Single women are denoted by "Miss") and return it."""
    """Returns the number of survived single women over age_threshold embarked at place_embarked
    (Single women are denoted by "Miss")

    >>> number_single_embarked_survived("Southampton", 40, titanic_data)
    4
    >>> number_single_embarked_survived("Cherbourg", 50, titanic_data)
    2
    >>> number_single_embarked_survived("Queenstown", 20, titanic_data)
    3
    """
    result_single = []
    for titanic in titanic_data:
        if titanic['age'] != "":
            if titanic['gender'] == 'F':
                if titanic['first'][1] == "i":
                    if titanic['embarked'] == place_embarked:
                        if float(titanic['age']) > age_threshold:
                            if titanic['survived'] == "yes":
                                result_single.append(titanic['first'])
    return len(result_single)


def class_survival_rate(passenger_class, titanic_data):
    """Use For to appreciate the data and make a condition if titanic['class'] == passenger_class that will have
    list name population to append fist name population data and make the conditions if titanic['survived'] == "yes"
    that will have list name survived to append fist name survived data
    and returns the survival rate of a given passenger_class."""
    """Returns the survival rate of a given passenger_class

    >>> survival_rate = class_survival_rate("1", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.63'
    >>> survival_rate = class_survival_rate("2", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.47'
    >>> survival_rate = class_survival_rate("3", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.24'
    """
    population = []
    survived = []
    for titanic in titanic_data:
        if titanic['class'] == passenger_class:
            population.append(titanic['first'])
            if titanic['survived'] == "yes":
                survived.append(titanic['first'])
    passenger_class = len(survived)/len(population)
    return passenger_class


def average_class_fare(passenger_class, titanic_data):
    """Use For to appreciate the data and make a condition if titanic['class'] == passenger_class that will have
    population.append(titanic['first']) and fare.append(float(titanic['fare'])).
    Last return average_fare is the sum(fare) divided by len(population)."""
    """Returns the average fare for a given class, 1, 2 or 3

    >>> average = average_class_fare("1", titanic_data)
    >>> f"{average:.2f}"
    '84.15'
    >>> average = average_class_fare("2", titanic_data)
    >>> f"{average:.2f}"
    '20.66'
    >>> average = average_class_fare("3", titanic_data)
    >>> f"{average:.2f}"
    '13.68'
    """
    population = []
    fare = []
    for titanic in titanic_data:
        if titanic['class'] == passenger_class:
            population.append(titanic['first'])
            fare.append(float(titanic['fare']))
    average_fare = sum(fare)/len(population)
    return average_fare


def gender_survival_number(passenger_gender, titanic_data):
    """Use For to appreciate the data and make a condition if titanic['gender'] == passenger_gender
    and  if titanic['survived'] == "yes" that will have survivors.append(titanic['first']).
    Last returns the number of survivors."""
    """Returns the number of survivors for a given gender, M (male) or F (female)

    >>> gender_survival_number('M', titanic_data)
    109
    >>> gender_survival_number('F', titanic_data)
    233
    """
    survivors = []
    for titanic in titanic_data:
        if titanic['gender'] == passenger_gender:
            if titanic['survived'] == "yes":
                survivors.append(titanic['first'])
    return len(survivors)


def common_last_name(titanic_data):
    """I use last list append last name if titanic['last'] == titanic['last']
    and I use .count to count the common last name then update the data in the values of dictionary.
    Last build list to append the number of common last name and make a condition if count == max(count_last)
    that will return most common last name."""
    """Returns most common last name

    >>> common_last_name(titanic_data)
    'Andersson'
    """
    last = []
    count_last = []
    dict_last = {}
    for titanic in titanic_data:
        dict_last[titanic['last']] = 0
        if titanic['last'] == titanic['last']:
            last.append(titanic['last'])
    for count in dict_last.keys():
        dict_last[count] = last.count(count)
        count_last.append(last.count(count))
    for last, count in dict_last.items():
        if count == max(count_last):
            return last


if __name__ == "__main__":
    import doctest
    doctest.testmod()