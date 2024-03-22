#!/usr/bin/python3
def search_replace(my_list, search, replace):
<<<<<<< HEAD
    new_list = my_list.copy()
    new_list = my_list.replace('search', 'replace')
    return (new_list)
=======
    new_list = []
    for x in range(len(my_list)):
        if my_list[x] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[x])
    return new_list
>>>>>>> 5d7bdb88599c6f90fe8a83a5bfa886b55efeb683
