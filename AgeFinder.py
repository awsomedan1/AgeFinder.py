import datetime    
def getages(year):
    newlist = []
    current_year = 2018
    for x in year:
        age = current_year - x
        newlist.append(age)
    return(newlist)
year = [2002, 2007, 1996]
print(getages(year))
