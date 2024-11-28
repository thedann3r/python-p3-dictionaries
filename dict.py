# def pour_coffee(size):
#     size_to_ounce_map = {
#         "tall": 12,
#         "grande": 16,
#         "venti": 20
#     }
#     return size_to_ounce_map.get(size, "Please enter a valid size")

# print(pour_coffee('grandee'))
# print(pour_coffee('tall'))
# print(pour_coffee('venti'))

# my_dict = {
#     "key_one": "value one",
#     "key_two": "value two",
#     }
# my_dict["key_one"] = 'i am diff'
# my_dict["key_three"] = 'i am new'

# print(my_dict["key_three"])

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

print([value for key, value in my_dict.items()])
