class NQueensBacktracking:
    def solve(self, n):
        result = []

        def backtrack(row, cols, diags, anti_diags):
            if row == n:
                result.append(cols)
                return
            for col in range(n):
                if col not in cols and row - col not in diags and row + col not in anti_diags:
                    backtrack(row + 1, cols + [col], diags + [row - col], anti_diags + [row + col])

        backtrack(0, [], [], [])
        return result

    def visualize_solution(self, solution):
        board = [['-' for _ in range(len(solution))] for _ in range(len(solution))]
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        for row in board:
            print(' '.join(row))

# Example usage:
n_queens_backtracking = NQueensBacktracking()
solutions = n_queens_backtracking.solve(8)
print("Backtracking solutions for N=8:")
for solution in solutions:
    n_queens_backtracking.visualize_solution(solution)
    print()
