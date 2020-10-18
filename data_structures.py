############## LISTS ######################

# def set_list(message):
#     some_list = input(message)
#     some_list = list(some_list)
#     return True


# message = "Please enter a sequence of characters: "
# my_list = [1, 2, 3, 4, 5, 5, 5, 5]
# my_list.append(['insert', 'remove', 'extend', 'clear', 'pop', 'append'])
# popped = my_list.pop(0)
# print(popped, my_list.count(5), '')
# del my_list
# print(my_list)


################ TUPLES #####################
# my_tuple = (12345, 23457, 'hella'
# print(my_tuple)


############### SETS ########################
set_a = {1, 3, 4, 5, 6}
set_b = {0, 5, 2, 3, 7}
# print((set_a | set_b))

############### DICTIONARIES #################
question = ["name", "age", "position"]
answer = ["wisdom", "20", "Senior Developer"]

my_dict2 = {"name": "Okon", "age": 27, "position": "1st"}

# for i, j in zip(question, answer):
#     print('What is your {x}? My {x} is {y}'.format(x=i, y=j))

# new_list = map(lambda q: q*3, question)
# print(list(new_list))


def get_name(**name):
    return name


print([('{key}:{val}'.format(key=x, val=y))
       for x, y in get_name(name="wisdom", name1="King", name2="Heneh").items()])

# print("name" not in my_dict2)

################ LIST COMPREHENSIONS ##################


SOME_LIST = [("W"*i) for i in range(10)]
# print(SOME_LIST)
