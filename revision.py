import glob
import pandas as pd
from dailyVocab import self_test

def combine():
    all_filenames = [i for i in glob.glob('*-*.csv')]

    #combine all files in the list
    colnames=['CH', 'EN']
    combined_df = pd.concat([pd.read_csv(f,names=colnames,header=None) for f in all_filenames ])

    #reset the index
    combined_df.reset_index(inplace=True,drop=True)
    return combined_df

def random_test(total_words):
    # word_dic = combined_csv
    # list to do = all chinese or there's an option on how many to test out each day
    words = input('Enter:')
    # listTodo = total_words['CH']
    try:
        # words = int(words)
        if words.isdigit():
            if int(words) == 0:
                print('Value cannot be 0')
                random_test(total_words)
            #sample the df
            total_words = total_words.sample(n=int(words), replace = False)
            listTodo = total_words['CH']
        else:
            listTodo = total_words['CH']
        word_dic = pd.Series(total_words.EN.values, index=total_words.CH).to_dict()

        # test it
        wrong_list = set()
        self_test(wrong_list, listTodo, word_dic)
    except ValueError:
            print("Oops!  This is an invalid value.  Try again...")
            random_test(total_words)

def print_out():
    total_words = combine()
    print(f'''
    How many words do you want to test it out today?
    There are total {len(total_words)}.
    Enter the number e.g 30, or any character to test out all words.''')
    random_test(total_words)

if __name__ == '__main__':
    print_out()