import time
import statistics
import json

def solve_nqueens(n):
    board = [-1] * n
    solutions = []
    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i]-col) == abs(i-row):
                return False
        return True
    def backtrack(row=0):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row+1)
                board[row] = -1
    backtrack()
    return len(solutions)

def benchmark(n, reps=15):  
    times = []
    for _ in range(reps):
        t0 = time.perf_counter()
        solve_nqueens(n)
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000)
    return {"n": n, "mean_ms": statistics.mean(times), "std_ms": statistics.pstdev(times)}

if __name__ == "__main__":
    
    results = []
    for n in [4, 6, 8, 10, 12, 14, 15]:
        print(f"Testando {n}x{n}...")
        res = benchmark(n)
        results.append(res)
        print(f"{n}x{n}: {res['mean_ms']:.2f} ± {res['std_ms']:.2f} ms")
    with open("tempos_python.json", "w") as f:
        json.dump(results, f, indent=2)
