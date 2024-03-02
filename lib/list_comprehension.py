#!/usr/bin/env python3

#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:  
            evens.append(num)  
    return evens    
print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentence_list):
     exclamation = []
     for sentence in sentence_list:
        exclamation.append(sentence + "!") 
     return exclamation

    