def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)

def reverse(arr):
    reverse_array(arr, 0, len(arr)-1)
    return arr

