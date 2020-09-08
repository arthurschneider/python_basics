#! /usr/bin/python3

list = [(4,5),(8,4,9),(3,2)]


def print_list_and_tupels():
    for tupel in list:
        print(tupel)
        for number in tupel:
            print(number)

def print_last_tupel_value():
    for tupel in list:
        print(tupel[-1])

def print_at_index():
    print(list.index((8,4,9)))

def sort_by_last_tupel_value():
    sorted = []
    for tupel in list:
        if len(sorted) == 0:
            sorted.append(tupel)
        for sort in sorted:
            print(sort)
            if tupel[-1] > sort[-1]:
                index = sorted.index(sort)
                sorted.insert(index+1, tupel)
                break
    return sorted

def custom_sort():
    local_list = sorted(list, key=lambda x : x[-1])
    return local_list

if __name__ == "__main__":
    #print_list_and_tupels()
    #print_last_tupel_value()
    #print(sort_by_last_tupel_value())
    #print_at_index()
    print(custom_sort())
