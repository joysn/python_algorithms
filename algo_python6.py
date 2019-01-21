def AutoComplete(dict_set, prefix):
    op_list = list()
    for word in dict_set:
        if word.startswith(prefix):
            op_list.append(word)

    return op_list


dict_set = {"abc","acd","bcd","def","a","aba"}
print(AutoComplete(dict_set,"a"))
print(AutoComplete(dict_set,"b"))