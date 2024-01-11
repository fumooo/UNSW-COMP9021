# Will be tested with year between 1913 and 2013.


import csv


def f(year):
    # '''
    # >>> f(1914)
    # In 1914, maximum inflation was: 2.0
    # It was achieved in the following months: Aug
    # >>> f(1922)
    # In 1922, maximum inflation was: 0.6
    # It was achieved in the following months: Jul, Oct, Nov, Dec
    # >>> f(1995)
    # In 1995, maximum inflation was: 0.4
    # It was achieved in the following months: Jan, Feb
    # >>> f(2013)
    # In 2013, maximum inflation was: 0.82
    # It was achieved in the following months: Feb
    # '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',\
             'Sep', 'Oct', 'Nov', 'Dec'
    # INSERT YOUR CODE HERE
    dicStock = []
    with open("cpiai.csv",'r') as file:
        reader = csv.DictReader(file)

        # for rol in reader:
        #     print(rol['Date'][5:7])
        for rol in reader:
            if(rol["Date"][:4] == str(year)):
                # print(rol["Date"],rol["Index"],rol["Inflation"])
                dic = {"Date":str, "Index":str, "Inflation":float}
                dic["Date"] = rol["Date"]
                dic["Index"] = rol["Index"]
                dic["Inflation"] = float(rol["Inflation"])
                dicStock.append(dic)
        dicStock = sorted(dicStock, key=lambda x:x["Inflation"])
        print(dicStock[-1]["Inflation"])
        # print(reader)
if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    f(2013)