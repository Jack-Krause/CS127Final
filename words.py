import random


def get_kitchen_word():
    word_list = ["spoon", "fork", "spatula", "toaster", "knife", "griddle", "oven", "pot", "skillet", "bowl"]
    num = enumerate(word_list)
    counter = 0
    for key in num:
        counter += 1
    # print(counter)
    index = random.randrange(0, len(word_list))
    return word_list[index]


def get_special_word():
    special_word_list = ["left", "grab", "computer", "road", "mouse", "kangaroo", "key", "door", "chair", "cord",]
    num = enumerate(special_word_list)
    counter = 0
    for key in num:
        counter += 1
    # print(counter)



with open("word_list.txt", "r") as words_file:
    read_data = words_file.read()
    x = []
    for line in read_date:
        x += line
    print(x)





# print(read_data)
# for word in read_data:
# #     print(i)
# x = read_data
# for i in x:
#     print(i)
def get_word_from_file(filename):
    pass
