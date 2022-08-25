"""
arr = [21,38,29,17,4,25,11,32,9]


def shell_sort(arr):
    gap = 3
    size = len(arr)
    for i in range(gap , size):
        anchor = arr[i]
        j = i
        while j >= gap and arr[j-gap] > anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor

    print(f"array is {arr} " ,  end=" ")




arr = [21,38,29,17,4,25,11,32,9]
shell_sort(arr)


"""

def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap , size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor

        gap = gap // 2

    print(arr , end=" ")


arr = [21,38,29,17,4,25,11,32,9]
shell_sort(arr)
#[4, 9, 11, 17, 21, 25, 29, 32, 38]
