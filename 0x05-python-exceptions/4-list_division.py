#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    This function divides two lists based on their index
    and handles exceptions
    """
    res = 0
    new_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
