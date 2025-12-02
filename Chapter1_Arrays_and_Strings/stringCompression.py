# O(n) time complexity, O(n^2) space in worst case scenario
def stringCompression(text: str) -> str:
    freq_list = []
    char_list = []
    text += ' '

    i = 0
    while i < len(text) - 1:
        count = 1
        while text[i] == text[i + 1]:
            count += 1
            i += 1

        freq_list.append(count)
        char_list.append(text[i])

        i += 1

    if len(text) <= len(freq_list) * 2:
        # remove the space added for the while loop
        return text.strip()

    new_str = ' '
    for i in range(len(freq_list)):
        new_str += (char_list[i] + str(freq_list[i]))

    return new_str.strip()


def runTests() -> int:
    class Test:
        def __init__(self, str, expectedStr):
            self.str = str
            self.expectedStr = expectedStr

        def run(self) -> bool:
            print(stringCompression(self.str))
            return stringCompressionOptimized(self.str) == self.expectedStr

    Tests = [
        Test("aaabbbcccd", "a3b3c3d1"),
        Test("aabbccd", "aabbccd"),
        Test("aaabcd", "aaabcd"),
        Test("AAbbcccdd", "A2b2c3d2"),
        Test("aaabbcccaaa", "a3b2c3a3")
    ]

    score = 0
    for test in Tests:
        score += (int(test.run()) * (100 // len(Tests)))

    return score


# Varianta optimizată - O(n) timp, O(n) spațiu
def stringCompressionOptimized(text: str) -> str:

    result = []
    i = 0

    while i < len(text):
        current_char = text[i]
        count = 1

        # Numără caractere consecutive identice
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1

        result.append(current_char + str(count))
        i += 1

    compressed = ''.join(result)
    return compressed if len(compressed) < len(text) else text


if __name__ == "__main__":
    print(f"Score: {runTests()} / 100 points!")