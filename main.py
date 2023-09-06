from csv import reader
def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    f = open(file_name,mode='r+')
    data = list(reader(f,delimiter=','))
    cou_index = data[0].index('country')
    country = []
    for i in data[1:]:
        country.append(i[cou_index])
    return country
print(get_country_column('data.csv'))
