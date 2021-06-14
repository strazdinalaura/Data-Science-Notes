from typing import Text


def return_dict_of_vals(tup1, tup2, tup3, tup4):
    #first set up the dictionary
    #4 tuples, put in a dict in a way that first element of the tuple is the key and the 2 value of the next tuple is a value 
    d = { 
        tup1[0]:tup1[1],
        tup2[0]:tup2[1],
        tup3[0]:tup3[1],
        tup4[0]:tup4[1]

    }

    return d

tup1 = ('value0', 'value1')
tup2 = ('value3', 'value4')
tup3 = ('value5', 'value6')
tup4 = ('value7', 'value8')

print(return_dict_of_vals(tup1, tup2, tup3, tup4))
#prints {'value0': 'value1', 'value3': 'value4', 'value5': 'value6', 'value7': 'value8'}

#########################################################

#### adding new items to the dict
some_dict = dict()
some_dict['new item'] = 1
print(some_dict)
some_dict['another item'] = 2
print(some_dict)

##### unapcking a tuple into key-value pair aka 
# adding a tuple to a dictionary = returns dictionary with the added tuple
other_d = {'frog':2, 'log':3}
other_tup = ('nog', 7)

other_d[other_tup[0]] = other_tup[1]
print(other_d)
#prints {'frog': 2, 'log': 3, 'nog': 7}

#########################################################


def letter_idx(txt):
    
    d = {}
    vowels = 'aeiouy'

    for idx, letter in enumerate(txt):
        if letter in vowels and letter not in d: 
            d[letter] = []

        #if we find the letter in vowels, we add the id to the letter 
        if letter in vowels:
            d[letter] += [idx]            #or d[letter].append(idx)


    return d

print(letter_idx("hello there!"))

#########################################################

def letter_idx(word):

    # 1. This is the vowel index accumulator
    vowel_dict = {}

    # 2. Use 'enumerate' since both index and character are used
    # Use 'word.lower()' since the function should be case-insensitive

    for idx, char in enumerate(word.lower()):
        if char in "aeiouy":
            # If the vowel is already in the dictionary, append the index
            if char in vowel_dict:
                vowel_dict[char].append(idx)
            # Otherwise, initialize the dictionary key with a new list containing the index
            # aka I need to add a char to the dictionary, and start a list with this index."
            else:
                vowel_dict[char] = [idx]

    return vowel_dict
print(letter_idx("Hello"))


#########################################################

   
def check_dict(d, pot_key):

    if pot_key in d:
        return d[pot_key]
    else:
        return "not in dict"


d1 = {'key': 'key3', 'key1':'value1'}
pot_key2 = 'key1'
print(check_dict(d1, pot_key2))

#########################################################

def observation_adder(dict_of_obs, seen):

    obs_count = 0

    for key in dict_of_obs:
        if dict_of_obs[key] == seen:
            obs_count += 1
    return obs_count
    

test_dict = {'person': 'Laura', 'age': 24, 'test':'seen'}
seen_test = 'Laura'
print(observation_adder(test_dict, seen_test))















#######################################################"""


