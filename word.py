import pandas as pd
import sys
import re
from collections import Counter


def self_test(w,wordList):
    text = ""
    wordList = [x for x in wordList if x == x]
    enter = []
    for word in wordList:
        while text!= word:
            text = input()
            if text == 'h':
                print(word)
            elif text == 'q':
                sys.exit(0)
            elif text == word:
                enter.append(text)
                print(w,'\n',len(enter),'-',len(wordList),enter)
                break
            else:
                print(word[0]+'_'*(len(word)-2)+word[-1])

def print_key_value(dct):
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{}: {}".format(item, amount))


def main():
    #read in csv and convert them into two dictionary
    data = pd.read_csv("cp.csv")
    wordDic = data.to_dict('list')
    headingDic = {v: k for v, k in enumerate(list(data.columns))}
    print_key_value(headingDic)

    test = input('Enter your choice: ').lower()

    if test == 'y':
        for k,v in wordDic.items():
            print(k)
            self_test(k,v)

    elif re.search("[+-]", test):
        twoRange = test.split('-')
        for i in range(int(twoRange[0]),int(twoRange[-1])+1):
            w = headingDic[i]
            self_test(w, wordDic[w])

    else:
        test = int(test)-1
        w = headingDic[int(test)]
        self_test(w,wordDic[w])

if __name__ == "__main__":
    main()



