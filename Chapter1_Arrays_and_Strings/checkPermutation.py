
# O(n * log n)
def isPermutation(str1, str2) -> bool:
    str1 = "".join(sorted(str1))
    str2 = "".join(sorted(str2))

    return str1 == str2

# O(n)
def isPermutationHashTable(str1, str2) -> bool:
    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True





str1 = input("Input string 1: ")
str2 = input("Input string 2: ")

if isPermutationHashTable(str1, str2):
    print("Strings are permutation of one another")
else:
    print("Diff shits!")