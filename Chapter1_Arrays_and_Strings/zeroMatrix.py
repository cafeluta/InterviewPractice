import math

def zeroColumn(matrix, j):
    for i in range(len(matrix)):
        matrix[i][j] = 0

def zeroRow(matrix, i):
    for j in range(len(matrix[i])):
        matrix[i][j] = 0

# O(n^2) time complexity, O(1) additional space
def zeroMatrix(matrix):
    """
    Mark matrix[i][0] = matrix[0][j] = 0 if matrix[i][j] == 0
    We use first row and column as markers for which column and row to zero

    first_row_zero = true (first row contains a zero so we need to zero all row)
                   = false (no need to copy the entire row because all zero's put in it mean they should be there)

    first_column_zero = SAME AS FIRST_ROW_ZERO
    """
    if not matrix or any(len(row) == 0 for row in matrix):
        return matrix

    first_row_zero = any(matrix[0][j] == 0 for j in range(len(matrix[0])))
    first_column_zero = any(matrix[i][0] == 0 for i in range(len(matrix)))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            zeroRow(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            zeroColumn(matrix, j)

    if first_column_zero:
        zeroColumn(matrix, 0)
    if first_row_zero:
        zeroRow(matrix, 0)

def runTests() -> int:
    class Test:
        def __init__(self, matrix, solution):
            self.matrix = matrix
            self.solution = solution

        def run(self) -> bool:
            # Function mutates matrix in place; compare mutated input
            zeroMatrix(self.matrix)
            return self.matrix == self.solution

    Tests = [
        Test(
            [[1, 2, 0, 4],
             [5, 6, 7, 8],
             [0, 10, 11, 12],
             [13, 14, 15, 16]],
            [[0, 0, 0, 0],
             [0, 6, 0, 8],
             [0, 0, 0, 0],
             [0, 14, 0, 16]]
        ),
        # No zeros: matrix unchanged
        Test(
            [[1, 2],
             [3, 4]],
            [[1, 2],
             [3, 4]]
        ),
        # Single zero at center
        Test(
            [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 9]],
            [[1, 0, 3],
             [0, 0, 0],
             [7, 0, 9]]
        ),
        # Zero at corner
        Test(
            [[0, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[0, 0, 0],
             [0, 5, 6],
             [0, 8, 9]]
        ),
        # Multiple zeros in same row/column
        Test(
            [[1, 0, 3],
             [0, 5, 6],
             [7, 8, 9]],
              [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 9]]
        ),
        # Rectangular matrix 2x3
        Test(
            [[1, 2, 0],
             [4, 5, 6]],
            [[0, 0, 0],
             [4, 5, 0]]
        ),
        # Rectangular matrix 3x2
        Test(
            [[1, 0],
             [3, 4],
             [5, 6]],
            [[0, 0],
             [3, 0],
             [5, 0]]
        ),
        # Empty matrix
        Test([], []),
        # Single empty row
        Test([[]], [[]]),
        # All zeros
        Test(
            [[0, 0],
             [0, 0]],
            [[0, 0],
             [0, 0]]
        ),
    ]

    score = 0
    for idx, test in enumerate(Tests, 1):
        ok = test.run()
        print(f"Test {idx}: {'OK' if ok else 'FAIL'} -> {test.matrix} vs {test.solution}")
        score += (int(ok) * (100 / len(Tests)))

    return score


if __name__ == "__main__":
    print(f"You got: {int(math.floor(runTests()))}/100p!")