def mergeRanges(times):
    sortedMeetings = sorted(times)
    mergedMeetings = [sortedMeetings[0]]

    for currentStartTime,currentEndTime in sortedMeetings[1:]:
        lastStartTime, lastEndTime = mergedMeetings[-1]

        if lastEndTime >= currentStartTime:
            mergedMeetings[-1] = (lastStartTime,max(currentEndTime,lastEndTime))
        else:
            mergedMeetings.append((currentStartTime,currentEndTime))

    return mergedMeetings

test_list1 = [(1, 10), (2, 6), (3, 5), (7, 9)]
test_list2 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
test_list3 = [(1, 2), (2, 3)]
test_list4 = [(1, 5), (2, 3)]
print(mergeRanges(test_list1))
print(mergeRanges(test_list2))
print(mergeRanges(test_list3))
print(mergeRanges(test_list4))
