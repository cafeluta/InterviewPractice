import math

def stringRotation(str1, str2) -> bool:
    """
    Concat str2 with str2 and check if str1 is inside
    """
    str2str2 = str2 + str2
    return str1 in str2str2

def runTests() -> int:
    class Test:
        def __init__(self, str1, str2, solution):
            self.str1 = str1
            self.str2 = str2
            self.solution = solution

        def run(self) -> bool:
            return stringRotation(self.str1, self.str2) == self.solution

    Tests = [
        Test("waterbottle", "erbottlewat", True),
        Test("hello", "llohe", True),
        Test("hello", "helol", False),
        Test("abcde", "abced", False),
        Test("", "", True),
        Test("a", "a", True),
        Test("a", "b", False)
    ]

    score = 0
    for idx, test in enumerate(Tests, 1):
        ok = test.run()
        print(f"Test {idx}: {'OK' if ok else 'FAIL'}")
        score += (int(ok) * (100 / len(Tests)))

    return score


if __name__ == "__main__":
    print(f"You got: {int(math.floor(runTests()))}/100p!")