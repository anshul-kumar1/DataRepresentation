# Question 3
def frequency_count(A: list) -> list:
    final = []
    sorted_A = merge_sort(A)
    dict = {x:A.count(x) for x in sorted_A}
    for k in dict.keys():
        final.append((k, dict.get(k)))
    return final

# Question 4
def shuffle(l1: list, l2: list) -> list:
    final = []
    i = 0

    if not l1 and not l2:
        return final

    if l1 and not l2:
        return l1

    if l2 and not l1:
        return l2

    while True:
        final.append(l1[i])
        final.append(l2[i])
        i = i + 1
        if i == len(l1) or i == len(l2):
            break

    if len(l1) > len(l2):
        final.extend(l1[i:len(l1)])
    elif len(l2) > len(l1):
        final.extend(l2[i:])
    return final


# Question 5
def helper(l1: list, l2: list) -> list:
    # O(N) Time Complexity
    final = []
    i = 0
    j = 0

    while True:
        if l1[i] <= l2[j]:
            final.append(l1[i])
            i = i + 1
        else:
            final.append(l2[j])
            j = j + 1
        if i == len(l1) or j == len(l2):
            break
    if i == len(l1) and j != len(l2):
        final.extend(l2[j:len(l2)])
    elif j == len(l2) and i != len(l1):
        final.extend(l1[i:len(l1)])

    return final

def merge_sort(l: list) -> list:
    # O(N log N) Time Complexity
    final = [[elem] for elem in l]
    temp = []
    i = 0
    if len(l) <= 1:
        return l
    while True:
        temp.append(helper(final[i], final[i + 1]))
        i = i + 2
        if i == len(final):
            final = temp
            temp = []
            i = 0
        elif (i == len(final) - 1):
            temp[len(temp)-1] = helper(temp[len(temp)-1], final[len(final)-1])
            final = temp
            temp = []
            i = 0
        if len(final[0]) == len(l):
            break

    return final[0]