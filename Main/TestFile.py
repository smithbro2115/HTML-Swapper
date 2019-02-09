l_1 = [4, 5, 1, 6, 3]
l_2 = [90, 10, 1, 60, 3]
l_3 = [4, 50, 1, 60, 3]

master = [l_1, l_2, l_3]
other_list = master[1:]
master_set = tuple(other_list)
print(*master[1:])
master_set_1 = set(master[0])
print(list(set(master[0]).intersection(*master[1:])))
