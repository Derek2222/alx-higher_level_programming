#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))


