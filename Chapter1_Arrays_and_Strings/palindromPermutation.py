# O(n) time complexity , O(k) space, where k = unique characters inside text
def checkForPalindromePermutation(str: str) -> bool:
    """
            A given string need to be converted to lower case characters and if one
        character appears an odd number of times we can place that character in the middle of
        the palindrome, but if multiple odd frequency characters appear than our string can
        no longer be a PERMUTATION OF A PALINDROME
    """
    str = str.lower().strip().replace(' ', '')

    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1

    middle_character_found = False
    for ch in freq:
        if freq[ch] % 2 != 0 and middle_character_found == False:
            middle_character_found = True
        elif freq[ch] % 2 != 0:
            return False

    return True

# O(n) time complexity as well
# every character in alphabet has its position in bitVector
# 1 = odd count, 0 = even count
def checkForPalindromePermutationBitVector(str: str) -> bool:
    bitVector = createBitVector(str)
    return bitVector == 0 or checkExactlyOneBitSet(bitVector)

def createBitVector(str: str) -> int:
    bitVector = 0
    str = str.lower().strip().replace(' ', '')
    for ch in str:
        index = ord(ch) - ord('a')
        bitVector = toggle(bitVector, index)

    return  bitVector


def toggle(bitVector, index) -> int:
    if index < 0:
        return bitVector

    mask = 1 << index
    if (bitVector & mask) == 0:
        bitVector |= mask
    else:
        bitVector &= ~mask

    return bitVector

# 00010000 - 1 = 00001111
# 00010000 & 00001111 = 0 -> only one bit was 1 in bitVector
def checkExactlyOneBitSet(bitVector: int) -> bool:
    return (bitVector & (bitVector - 1)) == 0

if __name__ == "__main__":
    text = input("Input a text: ")
    print(checkForPalindromePermutationBitVector(text))