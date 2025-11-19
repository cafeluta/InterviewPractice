# Print pairs inside an array with a given k difference between terms

def print_k_diff_pairs(arr, k):
    # hash table
    arr_set = set(arr)

    for x in arr:
        target1 = x + k
        target2 = x - k

        if target1 in arr_set:
            print(x, target1)
        elif target2 in arr_set:
            print(x, target2)

array_example = [1, 7, 5, 9, 2, 12, 3]
k_example = 2

print_k_diff_pairs(array_example, k_example)
