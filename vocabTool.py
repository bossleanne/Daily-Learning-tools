import pandas as pd
from datetime import datetime,date
import re
import csv
from dailyVocab import test
import os

def takeInput(df):
    # Select first column of the dataframe as a series
    first_column = df.iloc[:, 0]

    #remove the title as the title has ':'
    wordlist = [x for x in first_column if not '：' in x]
    #remove the number in the string
    wordlist = [re.sub(r'\d', '', i).replace(' ','') for i in wordlist]

    #find the days differences
    d0 = date(2021,6,15)
    today = datetime.now().date()
    delta = (today - d0).days
    #find out start and end line for each day
    start = 20 * delta - 20
    end = 20 * delta
    #create new list
    listTodo = wordlist[start:end]
    word_dic={}


    #take the input and combine the daily word list to a dictionary
    print("Start to record today's word list!")
    for i in listTodo:
        answer = input(i+'\n')
        word_dic[i] = answer

    outputDate = str(datetime.now().date())


    with open(outputDate+'.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in word_dic.items():
            writer.writerow([key, value])




def main():
    dir_path = os.getcwd()
    df = pd.read_csv(dir_path+'/Book1.csv', header=None)
    takeInput(df)
    dftest = pd.read_csv(dir_path+'/' + str(datetime.now().date()) + '.csv', header=None, index_col=None)

    TestFLag = input("""Do you want to start today's test? Enter y or n to continue\n
    """)
    test(dftest) if TestFLag == 'y' else exit()
main()
