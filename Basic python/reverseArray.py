arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)



def reverse_array(arr, l, r):
    if l >= r:
        return

    arr[l], arr[r] = arr[r], arr[l]

    reverse_array(arr, l + 1, r - 1)


arr = [3, 4, 6, 8,9,10]

reverse_array(arr, 0, len(arr) - 1)

print(arr)