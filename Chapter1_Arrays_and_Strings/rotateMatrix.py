import math

# O(n) complexity, O(1) additional space
def rotateMatrix(matrix):
    # transpose matrix
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse every line of the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix

def runTests() -> int:
    class Test:
        def __init__(self, matrix, solution):
            self.matrix = matrix
            self.solution = solution

        def run(self) -> bool:
            return rotateMatrix(self.matrix) == self.solution

    Tests = [
        # 1x1 matrix
        Test([[1]], [[1]]),
        # 2x2 matrix
        Test([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        # 3x3 matrix (existing case)
        Test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        # 4x4 matrix
        Test(
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]],
            [[13, 9, 5, 1],
             [14, 10, 6, 2],
             [15, 11, 7, 3],
             [16, 12, 8, 4]]
        ),
        # Empty matrix
        Test([], []),
        # Single empty row (edge but treat as already rotated)
        Test([[]], [[]])
    ]

    score = 0
    for test in Tests:
        score += (int(test.run()) * (100 / len(Tests)))

    return score


if __name__ == "__main__":
    print(f"You got: {int(math.floor(runTests()))}/100p!")