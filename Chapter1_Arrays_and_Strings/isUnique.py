# suppose we only have characters a->z, we can store the freq inside a int value
def hasUniqueCharsBitVector(str) -> bool:
    checker = 0
    for ch in str:
        value = ord(ch) - ord('a')
        if (checker & (1 << value)):
            return False
        checker |= (1 << value)

    return True



str = input("Input a string: ")

if hasUniqueCharsBitVector(str):
    print("String has only unique characters!")
else:
    print("String has duplicate characters!")