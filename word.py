import pandas as pd
import sys
import pprint

def self_test(wordList):
    text = ""
    for word in wordList:
        if str(word) != 'nan':
            while text!= word:
#                print(word[0]+'_'*(len(word)-2)+word[-1])
                text = input()
                if text == 'h':
                    print(word)
#                elif text == ' ':
#                    print(word[0]+'_'*(len(word)-2)+word[-1])
                elif text == 'q':
                    sys.exit(0)
                elif text == word:
#                    print('')
                    break
                else:
                    print(word[0]+'_'*(len(word)-2)+word[-1])
                
#                    print(' '*len(word),"| Wrong |  ",word[0]+'_'*(len(word)-2)+word[-1])
#                    print()

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
            self_test(v)
    else:
        w = headingDic[int(test)]
        self_test(wordDic[w])

if __name__ == "__main__":
    main()



