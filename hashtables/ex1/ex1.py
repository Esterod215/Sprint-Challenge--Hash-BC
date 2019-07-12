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
    

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    if length < 2:
        return None
    
    for value in range(0, length):
        hash_table_insert(ht, weights[value], value)
    

    for value in range(0, length):
        weight = limit - weights[value]

        if hash_table_retrieve(ht, weight):
            if value > hash_table_retrieve(ht, weight):
                return (value, hash_table_retrieve(ht, weight))
            else:
                return (hash_table_retrieve(ht, weight), value)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        return answer
    else:
        print("None")
