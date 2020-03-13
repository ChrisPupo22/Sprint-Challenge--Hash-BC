#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
   

    
    for i in range(len(weights)): 
        for j in range(len(weights[1::])):
            if i + j == limit: 
                ht.hash_table_insert(ht, i, weights[i])
                print(ht)
            else: 
                return None


    return ht


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_5 = [5, 0, 9, 12]
get_indices_of_item_weights(weights_5, 4, 14)

