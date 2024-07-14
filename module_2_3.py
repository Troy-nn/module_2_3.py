my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
kdn = 0

while kdn < len(my_list):
    if my_list[kdn] > 0:
        print(my_list[kdn])
        kdn += 1
    elif my_list[kdn] == 0:
        kdn += 1
    else:
        break
