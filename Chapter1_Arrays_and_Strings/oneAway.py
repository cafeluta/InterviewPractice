
def checkOneAway(str1: str, str2: str) -> bool:
    """Check if str1 and str2 are one edit away (insert, remove, or replace).

    Time: O(n), Space: O(1)
    """
    # Ensure str1 is shorter or equal length
    if len(str1) > len(str2):
        return checkOneAway(str2, str1)

    len_diff = len(str2) - len(str1)
    if len_diff > 1:
        return False

    found_difference = False
    i = j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if found_difference:
                return False
            found_difference = True

            # If lengths are same, move both pointers (replace case)
            # If lengths differ, move only j (insert case in str2)
            if len_diff == 0:
                i += 1
            j += 1
        else:
            i += 1
            j += 1

    return True



def runTests() -> int:
    class Test:
        def __init__(self, str1, str2, value: bool):
            self.str1 = str1
            self.str2 = str2
            self.value = value

        def run(self) -> bool:
            print("Test got: ", checkOneAway(self.str1, self.str2))
            return checkOneAway(self.str1, self.str2) == self.value

    Tests = [
        Test("pale", "ple", True),
        Test("pales", "pale", True),
        Test("pale", "bale", True),
        Test("pale", "bake", False),
        Test("pale", "bal", False)
    ]

    score = 0
    for test in Tests:
        score += (int(test.run()) * (100 // len(Tests)))

    return score


if __name__ == "__main__":
    print(f"You got: {runTests()}/100p!")
