# Written by *** for COMP9021
#
# Prompts the user for two capitalised strings of letters,
# say s1 and s2, then for two years in the range 1947--2021,
# say Y1 and Y2, with s1 and s2 and with Y1 and Y2 being separated
# by at least one space, and with possibly any extra spaces
# between s1 and s2, between Y1 and Y2, at the start of either input,
# and at the end of either input.
# - s1 can be lexicographically smaller than or equal to s2 
#   or the other way around;
# - Y1 can be smaller than or equal to Y2 or the other way around.
#
# Outputs an error message if input is incorrect.
# Otherwise, finds out amongst the names that are lexicographically
# between the first name that starts with s1
# and the last name that starts with s2, which name has been given
# as both a female name and a male name in a year between Y1 and Y2
# included. If there is such a name and year, then outputs all such
# names and years for which the absolute value of the difference
# between
# - the ratio defined as the count of the name as a female name
#   in that year over the count of all female names in that year,
# - the ratio defined as the count of the name as a male name
#   in that year over the count of all male names in that year,
# is minimal (so essentially, the popularities in that year
# of the name as a female name and of the name as a male name
# are as close as possible).
# Outputs the name, the year, and both ratios as percentages
# printed out with 5 digits after the decimal point.
# In case there are many solutions (that is, same minimal
# difference in popularities), then outputs all solutions
# in increasing lexicographic order of names, and for
# a given name, in increasing order of years.
#
# The directory named names is stored in the working directory.
#
# IF YOU USE ABSOLUTE PATHS, YOUR PROGRAM CAN ONLY FAIL TO RUN PROPERLY
# ON MY MACHINE AND YOU WILL SCORE 0 TO THE QUIZ, WITH NO CHANCE FOR YOU
# TO FIX THIS MISTAKE AFTER RESULTS HAVE BEEN RELEASED.
#
# YOU CANNOT USE pandas FOR THIS QUIZ; IF YOU DO, YOU WILL SCORE 0
# TO THE QUIZ.
import sys
from collections import defaultdict
from pathlib import Path
import csv


# INSERT YOUR CODE HERE
def IsCapital(StrCapital1,StrCapital2):
    if(StrCapital1 == None or StrCapital2 == None):
        print("Incorrect input, leaving it there.")
        sys.exit()
    elif (StrCapital1[0].isupper() and StrCapital2[0].isupper()):
        for i in range(1,len(StrCapital1)):
            if(StrCapital1[i].isupper()):
                print("Incorrect input, leaving it there.")
                sys.exit()
        for i in range(1,len(StrCapital2)):
            if(StrCapital2[i].isupper()):
                print("Incorrect input, leaving it there.")
                sys.exit()
        pass
    else:
        print("Incorrect input, leaving it there.")
        sys.exit()
def IsFitYear(Y1,Y2): #1947--2021
    # print(Y1,Y2)
    Year = []
    if(Y1 < 1947 or Y1 > 2021 or Y2 < 1947 or Y2 > 2021):
        print("Incorrect input, leaving it there.")
        sys.exit()
    elif(Y1 == Y2):
        Year.append(Y1)
    elif(Y1 > Y2):
        Year.append(Y2)
        Year.append(Y1)
    elif (Y1 < Y2):
        Year.append(Y1)
        Year.append(Y2)
    return Year
def GetMinimumRatio(Year):
    Y1 = Year
    filename = 'yob' + str(Y1) + '.txt'
    # print(filename)

    StockList = []  # storing the list
    current_directory = Path.cwd()
    names_directory = current_directory / "names"
    Y_file = names_directory / filename
    with open(Y_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            StockList.append(row)
    file.close()
    MaleSum = 0
    FemaleSum = 0
    if(StockList == []):
        return None
    StockList = sorted(StockList, key=lambda x: (x[0], x[1]))
    stockList = []
    # print(StockList)
    for stock in StockList:
        if (stock[1] == 'M'):
            MaleSum = MaleSum + float(stock[2])
        if (stock[1] == 'F'):
            FemaleSum = FemaleSum + float(stock[2])
        if s1 <= stock[0] <= s2 or stock[0].startswith(s2) :
            stockList.append(stock)
    # print(stockList)

    if(stockList == []):
        print("No name was given as both female and male names.")
        sys.exit()
    SameNameList = []  # store the SameNameList
    for i in range(0, len(stockList)):
        if (i == len(stockList) - 1):
            # print(i)
            break
        if (stockList[i][0] == stockList[i + 1][0]):
            SameNameDic = {"Name": "", "M": "", "F": "", "MaleRatio": float, "FemaleRatio": float, "AbVaule": float, "Year" : int}
            SameNameDic["Name"] = stockList[i][0]
            SameNameDic["F"] = stockList[i][2]
            SameNameDic["M"] = stockList[i + 1][2]
            SameNameDic["Year"] = Y1
            SameNameDic["MaleRatio"] = float(SameNameDic["M"]) / MaleSum
            SameNameDic["FemaleRatio"] = float(SameNameDic["F"]) / FemaleSum
            SameNameDic["AbVaule"] = abs(SameNameDic["MaleRatio"] - SameNameDic["FemaleRatio"])
            # print(SameNameDic)
            SameNameList.append(SameNameDic)
    SameNameList = sorted(SameNameList, key=lambda x: x['AbVaule'])
    if(SameNameList == []):
        print("No name was given as both female and male names.")
        sys.exit()
    # print("{:.7f}".format(MaleRatio), "{:.7f}".format(FemaleRatio))
    # print(MaleSum,FemaleSum)
    # print(SameNameList[0])
    return SameNameList[0]
def GetMinimunRatioByYears(Year):
    Y1 = Year
    filename = 'yob' + str(Y1) + '.txt'
    # print(filename)

    StockList = []  # storing the list
    current_directory = Path.cwd()
    names_directory = current_directory / "names"
    Y_file = names_directory / filename
    with open(Y_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            StockList.append(row)
    file.close()
    MaleSum = 0
    FemaleSum = 0
    if (StockList == []):
        return None
    StockList = sorted(StockList, key=lambda x: (x[0], x[1]))
    stockList = []
    # print(StockList)
    for stock in StockList:
        if (stock[1] == 'M'):
            MaleSum = MaleSum + float(stock[2])
        if (stock[1] == 'F'):
            FemaleSum = FemaleSum + float(stock[2])
        if s1 <= stock[0] <= s2 or stock[0].startswith(s2) :
            stockList.append(stock)
    # print(stockList)

    if(stockList == []):
        print("No name was given as both female and male names.")
        return None
    SameNameList = []  # store the SameNameList
    for i in range(0, len(stockList)):
        if (i == len(stockList) - 1):
            # print(i)
            break
        if (stockList[i][0] == stockList[i + 1][0]):
            SameNameDic = {"Name": "", "M": "", "F": "", "MaleRatio": float, "FemaleRatio": float, "AbVaule": float, "Year": int}
            SameNameDic["Name"] = stockList[i][0]
            SameNameDic["F"] = stockList[i][2]
            SameNameDic["M"] = stockList[i + 1][2]
            SameNameDic["Year"] = Y1
            SameNameDic["MaleRatio"] = float(SameNameDic["M"]) / MaleSum
            SameNameDic["FemaleRatio"] = float(SameNameDic["F"]) / FemaleSum
            SameNameDic["AbVaule"] = abs(SameNameDic["MaleRatio"] - SameNameDic["FemaleRatio"])
            # print(SameNameDic)
            SameNameList.append(SameNameDic)
    SameNameList = sorted(SameNameList, key=lambda x: x['AbVaule'])
    # print(SameNameList)
    # print("{:.7f}".format(MaleRatio), "{:.7f}".format(FemaleRatio))
    # print(MaleSum,FemaleSum)
    # print(SameNameList[0])
    return SameNameList[0]
if __name__ == '__main__':
    try:
        s1,s2 = map(str,input("Enter two capitalised strings of letters: ").split())
    except:
        print("Incorrect input, leaving it there.")
        sys.exit()
    IsCapital(s1,s2)
    if s1 >= s2:
        s1,s2 = s2,s1
    # print(s1,s2)
    try:
        Y1,Y2=map(int,input("Enter two integers between 1947 and 2021: ").split())
    except:
        print("Incorrect input, leaving it there.")
        sys.exit()

    Year = IsFitYear(Y1,Y2)
    # print(Year)
    if(len(Year) == 1 ):
        Dic = GetMinimumRatio(Year[0])
        # print(GetMinimumRatio(Year[0]))
        print("""Here are the names that were given as both
female and male names, for the smallest difference
of ratio as a female name over all female names
and ratio as a male name over all male names,
for the years when that happened:""")
        print("  " + Dic['Name'] + " in "+ str(Year[0]) + ", for ratios of")
        print("    - " + "{:.5%}".format(Dic["FemaleRatio"])+ " as a female name,")
        print("    - " + "{:.5%}".format(Dic["MaleRatio"])+ " as a male name.")

    elif(len(Year) == 2):
        # print(Year)
        MinRatioList = []
        for year in range(Year[0],Year[1]+1):
            # print(year)
            MinRatioList.append(GetMinimunRatioByYears(year))
            MinRatioList = sorted(MinRatioList, key=lambda x: x['AbVaule'])
        Dic = MinRatioList[0]
        # print(Dic)
        # print(GetMinimumRatio(Year[0]))
        print("""Here are the names that were given as both
female and male names, for the smallest difference
of ratio as a female name over all female names
and ratio as a male name over all male names,
for the years when that happened:""")
        print("  " + Dic['Name'] + " in " + str(Dic["Year"]) +", for ratios of")
        print("    - " + "{:.5%}".format(Dic["FemaleRatio"]) + " as a female name,")
        print("    - " + "{:.5%}".format(Dic["MaleRatio"]) + " as a male name.")
