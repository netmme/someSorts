# Auteur : Netmme


def merge(toSort, left, right, end):
    iLeft = left
    iRight = right
    while iLeft < right:
        while iRight < end and toSort[iLeft] > toSort[iRight]:
            iRight += 1
        if toSort[iLeft] > toSort[iRight - 1]:
            val = toSort.pop(iLeft)
            toSort.insert(iRight - 1, val)
            right -= 1
        else:
            iLeft += 1
    return toSort


def mergeSort(toSort):
    step = 2
    length = len(toSort)
    while step < length:
        left = 0
        right = step//2
        # print(step)
        while right < length:
            end = left + step if left + step < length else length
            # print(left, right, end)
            toSort = merge(toSort, left, right, end)
            left = end
            right += step
        step *= 2
    end = step//2
    if end < length:
        toSort = merge(toSort, 0, end, length)   
    return toSort
