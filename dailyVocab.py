import pandas as pd
import random
from datetime import datetime
import os

def self_test(wrong_list,listTodo, word_dic):
    answer = ''
    ##SECOND ROUND
    for i in listTodo:
        print(i)
        answer = input()

        if i in wrong_list:
            wrong_list.remove(i)

        while answer != word_dic[i]:
            if answer == 'h':
                print(word_dic[i])
            wrong_list.add(i)
            print(i)
            answer = input()

    if not wrong_list:
        for i in word_dic.values():
            print(i)
    else:
        print(wrong_list)

    if wrong_list:
        self_test(wrong_list,list(wrong_list), word_dic)


def test(df):
    print("\n\nStart to test today's word list!")
    listTodo = df[0]
    dfNew = df.rename(columns={0: 'zero', 1: 'one'})
    word_dic = pd.Series(dfNew.one.values, index=dfNew.zero).to_dict()

    #store wrong value
    wrong_list = set()

    # shuffle the list
    random.shuffle(listTodo)
    self_test(wrong_list,listTodo, word_dic)

def main():
    dir_path = os.getcwd()
    dftest = pd.read_csv(dir_path + '/' + str(datetime.now().date()) + '.csv', header=None, index_col=None)
    test(dftest)

if __name__ == '__main__':
    main()



