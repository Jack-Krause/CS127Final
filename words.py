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
    special_word_list = ["left", "grab", "computer", "road", "mouse", "kangaroo", "key", "door", "chair", "cord"]
    index = random.randrange(0, len(special_word_list))
    return special_word_list[index]
    num = enumerate(special_word_list)
    counter = 0
    for key in num:
        counter += 1
    # print(counter)

with open("word_list.txt", "r") as words_file:
    read_data = words_file.read()
    x = []
    read_file_list = read_data.split()

def get_word_from_file():
    index = random.randrange(0, len(read_file_list))
    return read_file_list[index]


