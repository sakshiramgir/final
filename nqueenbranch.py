class NQueensBranchBound:
    def solve(self, n):
        result = []

        def is_safe(row, col, queens):
            return all(row != r and col != c and abs(row - r) != abs(col - c) for r, c in queens)

        def backtrack(row, queens):
            if row == n:
                result.append(queens)
                return
            for col in range(n):
                if is_safe(row, col, queens):
                    backtrack(row + 1, queens + [(row, col)])

        backtrack(0, [])
        return result

    def visualize_solution(self, solution):
        board = [['-' for _ in range(len(solution))] for _ in range(len(solution))]
        for row, col in solution:
            board[row][col] = 'Q'
        for row in board:
            print(' '.join(row))

# Example usage:
n_queens_branch_bound = NQueensBranchBound()
solutions = n_queens_branch_bound.solve(8)
print("Branch and bound solutions for N=8:")
for solution in solutions:
    n_queens_branch_bound.visualize_solution(solution)
    print()

