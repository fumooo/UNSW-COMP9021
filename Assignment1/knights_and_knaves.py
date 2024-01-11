# EDIT THE FILE WITH YOUR SOLUTION
import sys
from os.path import exists
import re

# print(Paragraphy)

def GetSentence(text): #getSentence
    list_ret = list()
    SepList = list()

    pattern =  r'(\!"|\?"|\."|\.|\!|\?)'
    text = text.replace('\n',' ') #remove \n
    # print(text)
    text = re.sub(r'\s+', ' ', text)
    # print(text)
    # text = text.replace('"',' ') #remove ""
    sentences = re.split(pattern,text)
    sentences.append("")
    sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]

    for i in range(0,len(sentences)):
        sentences[i] = sentences[i].strip()
    return sentences
    # print(sentences)
    # names = re.findall(r'')
def GetNameBySentence(Sentences):
    name = []
    pattern1 = 'Sirs .* and \w*'
    pattern2 = 'Sir (\w*)'
    for i in Sentences:
        if(re.search(pattern1,i) != None):
            nameStr = re.findall(pattern1,i)[0]
            nameStr = nameStr.replace("Sirs ",'')
            nameStr = nameStr.replace("and ",'')
            nameStr = nameStr.replace(",",'')
            nameS = nameStr.split(" ")
            name.extend(nameS)
            # print(name)
        elif(re.search(pattern2,i) != None):
            nameList = re.findall(pattern2,i)
            # print(nameList)
            for i in nameList:
                name.append(i)
    nameSet = set(name)
    name = list(nameSet)
    name = sorted(name)
    return name

def NameRelationSpeakSentence(Sentences,names):
    NameSayingList = []
    # print(Sentences)
    for i in Sentences:
        if(re.search('".*"',i) != None):
            quote = re.findall('".*"',i)[0]
            quote = re.sub(r'[,.!?]','',quote)
            i = re.sub('".*"', '', i)
            for m in names:
                # print(m)
                if (re.search(m,i) != None):
                    # print(m,quote)
                    NameSaying = {"name": "", "quote": ""}
                    NameSaying["name"] = m
                    NameSaying["quote"] = quote
                    NameSayingList.append(NameSaying)
        else:
            continue
    # print(NameSayingList)
    return NameSayingList
def NameRelation(DicList,Name): #将每个人的说的条件映射过来
    Conlist = []
    pattern1 = '[Aa]t least one of (.*|us) is a (Knight|Knave)'
    pattern2 = '[Aa]t most one of (.*|us) is a (Knight|Knave)'
    pattern3 = '[Ee]xactly one of (.*|us) is a (Knight|Knave)'
    pattern4 = '[Aa]ll of us are (Knights|Knaves)'
    pattern5 = 'I am a (Knight|Knave)'
    pattern6 = 'Sir (\w+) is a (Knight|Knave)'
    pattern7 = '(.*) or (.*) is a (Knight|Knave)'
    pattern8 = 'Sir (.*) are (Knights|Knaves)'
    for dic in DicList:
        if(re.search(pattern1,dic['quote']) != None):
            tuple = re.findall(pattern1,dic['quote'])[0]
            # print(1)
            # print(tuple)
            if(tuple[0] == 'us' and tuple[1] == "Knight"): #CONFIRM
                nameStr = " + ".join(Name)
                LogicCon = ' ((' + dic['name']+ " == 1 and " + nameStr + ' >= 1) or (' + dic['name']+ " == 0 and " + nameStr  + ' < 1 )) '
                Conlist.append(LogicCon)
            if (tuple[0] == 'us' and tuple[1] == "Knave"):#CONFIRM
                nameStr = " + ".join(Name)
                LogicCon = ' ((' + dic['name']+ " == 1 and " + nameStr + ' <= ' + str(len(Name)-1)+ ')' + ' or (' + dic['name']+ " == 0 and " + nameStr + ' == ' + str(len(Name)) + ')) '
                Conlist.append(LogicCon)
            if(tuple[0] != 'us' and tuple[1] == "Knight"):#CONFIRM
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ','')
                nameStr = nameStr.replace('and ','')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0,len(namelist)):
                    if(namelist[i] == 'I'):
                       namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                # print("!!!" + nameStr)
                LogicCon = ' ((' + dic['name']+ " == 1 and " + nameStr + ' >= 1) or ' + '(' + dic['name']+ " == 0 and " + nameStr + ' < 1)) '
                Conlist.append(LogicCon)
            if (tuple[0] != 'us' and tuple[1] == "Knave"):#CONFIRM
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                LogicCon = ' ((' + dic['name']+ " == 1 and " + nameStr + ' <= ' + str(len(namelist)-1) + ') or '+ '(' + dic['name']+ " == 0 and " + nameStr  + ' >= ' + str(len(namelist)) + ')) '
            # print(LogicCon)
                Conlist.append(LogicCon)
            # LogicCon = '(' + dic['name'] + '==1 or ' + dic['name'] + '==0' + ')'
            continue
        if(re.search(pattern2,dic['quote']) != None):
            # print(re.search(pattern2,dic['quote']))
            tuple = re.findall(pattern2, dic['quote'])[0]
            # print(1)
            # print(tuple)
            if (tuple[0] == 'us' and tuple[1] == "Knight"):  # CONFIRM
                nameStr = " + ".join(Name)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' <= 1) or (' + dic[
                    'name'] + " == 0 and " + nameStr + ' > 1 )) '
                Conlist.append(LogicCon)
            if (tuple[0] == 'us' and tuple[1] == "Knave"):  # CONFIRM
                nameStr = " + ".join(Name)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' >= ' + str(len(Name) - 1) + ')' + ' or (' + \
                           dic['name'] + " == 0 and " + nameStr + ' < ' + str(len(Name)-1) + ')) '
                Conlist.append(LogicCon)
            if (tuple[0] != 'us' and tuple[1] == "Knight"):  # CONFIRM
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                # print("!!!" + nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' <= 1) or ' + '(' + dic[
                    'name'] + " == 0 and " + nameStr + ' > 1)) '
                Conlist.append(LogicCon)
            if (tuple[0] != 'us' and tuple[1] == "Knave"):  # CONFIRM
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' >= ' + str(
                    len(namelist) - 1) + ') or ' + '(' + dic['name'] + " == 0 and " + nameStr + ' < ' + str(
                    len(namelist)-1) + ')) '
                # print(LogicCon)
                Conlist.append(LogicCon)
            # LogicCon = '(' + dic['name'] + '==1 or ' + dic['name'] + '==0' + ')'
            continue
        if(re.search(pattern3,dic['quote']) != None):
            # print(re.search(pattern3,dic['quote']))
            tuple = re.findall(pattern3,dic['quote'])[0]
            # print(tuple)
            if(tuple[0] == 'us' and tuple[1] == "Knight"):
                nameStr = " + ".join(Name)
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == 1) or (' + dic['name'] + " == 0 and " + nameStr + ' != 1 )) '
                Conlist.append(LogicCon)
            if (tuple[0] == 'us' and tuple[1] == "Knave"):
                nameStr = " + ".join(Name)
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == '+ str(len(Name)-1) +') or (' + dic['name'] + " == 0 and " + nameStr + ' != '+ str(len(Name)-1) +' )) '
                Conlist.append(LogicCon)
            if (tuple[0] != 'us' and tuple[1] == "Knight"):
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                # print(nameStr)
                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")

                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                # print("!!!" + nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == 1) or ' + '(' + dic[
                    'name'] + " == 0 and " + nameStr + ' != 1)) '
                Conlist.append(LogicCon)
            if (tuple[0] != 'us' and tuple[1] == "Knave"):
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')

                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                # print("!!!" + nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == ' + str(len(namelist) - 1) + ') or (' + dic[
                    'name'] + " == 0 and " + nameStr + ' != ' + str(len(namelist)-1) + ' )) '
                Conlist.append(LogicCon)
            continue
        if(re.search(pattern4,dic['quote']) != None):
            # print(re.search(pattern4,dic['quote']))
            tuple = re.findall(pattern4,dic['quote'])
            # print(tuple)
            if(tuple[0] == 'Knights'):
                nameStr = ' + '.join(Name)
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == ' + str(len(Name)) + ') or ' + '(' + dic['name'] + " == 0 and " + nameStr + ' != ' + str(len(Name)) + ')) '
                Conlist.append(LogicCon)
            if (tuple[0] == 'Knaves'):
                nameStr = ' + '.join(Name)
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == 0'  + ') or ' + '(' + dic[
                    'name'] + " == 0 and " + nameStr + ' != 0'  + ')) '
                Conlist.append(LogicCon)
            continue
        if(re.search(pattern5,dic['quote']) != None):
            # print(re.findall(pattern5,dic['quote'])[0])
            if(re.findall(pattern5,dic['quote'])[0] == "Knave"):
                print("There is no solution.")
                sys.exit()
            else:
                # LogicCon = '('  + 'NameNumDic["'+dic['name'] + '"]' +  '==1 or ' + 'NameNumDic["' + dic['name'] + '"]' + '==0' + ')'
                LogicCon = '('  + dic['name'] +  '==1' + ' or ' + dic['name'] +'!=1)'
                Conlist.append(LogicCon)
                # print(LogicCon)
            continue
            # print(dic['name'],dic['quote'])
        if (re.search(pattern7, dic['quote']) != None):
            # print(re.search(pattern7,dic['quote']))
            tuple = re.findall(pattern7, dic['quote'])[0]
            # print("!!!!!!!!!")
            # print(tuple)

            if (tuple[2] == 'Knight'):
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('or ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)

                nameStr1 = tuple[1]
                nameStr1 = nameStr1.replace('Sir ', '')
                nameStr1 = nameStr1.replace('or ', '')
                nameStr1 = nameStr1.replace(',', '')
                nameStr = nameStr.replace('"', '')
                nameStr1 = re.sub(r'\s+', ' ', nameStr1).strip()
                namelist1 = nameStr1.split(" ")
                for i in range(0, len(namelist1)):
                    if (namelist1[i] == 'I'):
                        namelist1[i] = dic['name']
                nameStr1 = " + ".join(namelist1)

                nameStr = nameStr + ' + ' + nameStr1
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' >= 1' + ') or ' + '(' + dic[
                    'name'] + " == 0 and " + nameStr + ' < 1' + ')) '
                Conlist.append(LogicCon)
            if (tuple[2] == 'Knave'):
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('or ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = nameStr.replace('"', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)

                nameStr1 = tuple[1]
                nameStr1 = nameStr1.replace('Sir ', '')
                nameStr1 = nameStr1.replace('or ', '')
                nameStr1 = nameStr1.replace(',', '')
                nameStr1 = re.sub(r'\s+', ' ', nameStr1).strip()
                namelist1 = nameStr1.split(" ")
                for i in range(0, len(namelist1)):
                    if (namelist1[i] == 'I'):
                        namelist1[i] = dic['name']
                nameStr1 = " + ".join(namelist1)

                nameStr = nameStr + ' + ' + nameStr1
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' <= ' + str(len(namelist)+len(namelist1)-1) + ') or ' + '(' + \
                           dic[
                               'name'] + " == 0 and " + nameStr + ' > ' + str(len(namelist)+len(namelist1)-1) + ')) '
                Conlist.append(LogicCon)
            continue
        if (re.search(pattern8, dic['quote']) != None):  # Confirm

            # print(re.findall(pattern8,dic['quote']))
            tuple = re.findall(pattern8, dic['quote'])[0]
            if (tuple[1] == 'Knights'):
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = nameStr.replace('"', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == ' + str(len(namelist)) + ') or ' + '(' + \
                           dic['name'] + " == 0 and " + nameStr + ' != ' + str(len(namelist)) + ')) '
                Conlist.append(LogicCon)
            if (tuple[1] == 'Knaves'):
                nameStr = tuple[0]
                nameStr = nameStr.replace('Sir ', '')
                nameStr = nameStr.replace('and ', '')
                nameStr = nameStr.replace(',', '')
                nameStr = nameStr.replace('"', '')
                nameStr = re.sub(r'\s+', ' ', nameStr).strip()
                namelist = nameStr.split(" ")
                for i in range(0, len(namelist)):
                    if (namelist[i] == 'I'):
                        namelist[i] = dic['name']
                nameStr = " + ".join(namelist)
                # print(nameStr)
                LogicCon = ' ((' + dic['name'] + " == 1 and " + nameStr + ' == 0' + ') or ' + '(' + dic[
                    'name'] + " == 0 and " + nameStr + ' != 0' + ')) '
                Conlist.append(LogicCon)
            continue
        if(re.search(pattern6,dic['quote']) != None):
            # print(re.search(pattern6, dic['quote']))
            tuple = re.findall(pattern6,dic['quote'])[0]
            # print(111)
            # print(tuple)
            if(tuple[1]  == 'Knight'):
                LogicCon = ' ((' + dic['name'] + " == 1 and " + tuple[0] + ' == 1'  + ') or ' + '(' + \
                           dic[
                               'name'] + " == 0 and " + tuple[0] + ' == 0' + ')) '
                Conlist.append(LogicCon)
            if (tuple[1] == 'Knave'):
                LogicCon = ' ((' + dic['name'] + " == 1 and " + tuple[0] + ' == 0' + ') or ' + '(' + \
                           dic[
                               'name'] + " == 0 and " + tuple[0] + ' == 1' + ')) '
                Conlist.append(LogicCon)
            continue
    return Conlist

def LogicCalculate(Conlist,Name):

    NameNumDic = {}
    for name in Name:
        NameNumDic[name] = 0
    # print(NameNumDic)
    ConStr = ' and '.join(Conlist) #use and to link all the logic condition

    # print("逻辑条件是:" + ConStr)

    ForList = []
    ForStr = ''
    PrintCon = ''
    AppendStr= ''
    for i in range(0,len(Name)):
        # print("for " + Name[i] + " in range(0,2):")
        ForStr = ForStr + "for " + Name[i] + " in range(0,2):" + "\n" + "\t"*(i+1)
        PrintCon = PrintCon + Name[i] + ","
        AppendStr = AppendStr + "ForList.append(" + Name[i] + ")"+ "\n" + "\t"*(len(Name)+1)
        # ForList.append("for " + name + " in range(0,2):")
    ForStr = ForStr + "if(" +ConStr + "):" + "\n" + "\t"*(len(Name)+1)
    # ForStr = ForStr + "print(" + PrintCon[:-1] + ")" + "\n" + "\t"*(len(Name)+1)
    ForStr = ForStr + AppendStr

    print(ForStr)
    exec(ForStr)

    #用多维列表
    if(ForList == []):
        print("There is no solution.")
        return

    row_size = len(Name)
    QulifyList = [ForList[i:i+row_size] for i in range(0, len(ForList), row_size)]

    # print(QulifyList)

    if(len(QulifyList) == 1):
        print("There is a unique solution:")
        for m in QulifyList:
            for i in range(0,len(m)):
                if (m[i] == 0):
                    print("Sir " + Name[i] + " is a Knave.")
                else:
                    print("Sir " + Name[i] + " is a Knight.")
    if(len(QulifyList) > 1):
        print("There are " + str(len(QulifyList)) + " solutions.")


if __name__ == '__main__':
    #input the file name
    file_name = input("Which text file do you want to use for the puzzle? ")
    # Does the file exist
    if not exists(file_name):
        print('Incorrect input, giving up.')
        sys.exit()

    text = open(file_name)
    Paragraphy = text.read()
    #divide the Paragraphy into sentences
    Sentences = GetSentence(Paragraphy)
    # for i in Sentences:
    #     print(i)

    nameStr = "" #用于拼接name输出字符串
    name = GetNameBySentence(Sentences) # get the name list



    #输出的第一行
    for i in name:
        nameStr = nameStr + i + ' '
    print("The Sirs are: " + nameStr.strip())

    print("DicList：" + str(NameRelationSpeakSentence(Sentences, name)))#将名字和所说的话存入字典列表

    Conlist = NameRelation(NameRelationSpeakSentence(Sentences, name),name)#将所有逻辑返回一个逻辑列表
    if(Conlist == []):
        sys.exit()

    LogicCalculate(Conlist,name)#逻辑符运算
