#Merge two lists

def mergeLists(list1, list2):
    merged = []
    index1 = 0
    index2 = 0

    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] > list2[index2]:
            merged.append(list2[index2])
            index2 += 1
        else:
            merged.append(list1[index1])
            index1 += 1

    if index1 == len(list1):
        merged.extend(list2[index2:])
    elif index2 == len(list2):
        merged.extend(list1[index1:])

    print(merged)

list1 = [3, 4, 6, 10, 11, 15]
list2 = [1, 5, 8, 12, 14, 19]
mergeLists(list1,list2)