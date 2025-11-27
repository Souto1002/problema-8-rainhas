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
    print("=" * 60)
    print("  PROBLEMA DAS N RAINHAS - BENCHMARK (Python)")
    print("=" * 60)
    print()
    
    results = []
    for n in [4, 6, 8, 10, 12, 14]:
        print(f"  Testando tabuleiro {n}x{n}...", end=" ", flush=True)
        res = benchmark(n)
        results.append(res)
        print(f"✓")
        print(f"    Tempo médio: {res['mean_ms']:>10.2f} ms")
        print(f"    Desvio padrão: {res['std_ms']:>8.2f} ms")
        print()
    
    print("=" * 60)
    print("  Resumo dos resultados:")
    print("-" * 60)
    print(f"  {'Tamanho':<10} {'Tempo Médio (ms)':<20} {'Desvio Padrão (ms)':<20}")
    print("-" * 60)
    for res in results:
        print(f"  {res['n']}x{res['n']:<6} {res['mean_ms']:>15.2f} {res['std_ms']:>18.2f}")
    print("=" * 60)
    print()
    print("  Resultados salvos em: tempos_python.json")
    print()
    
    with open("tempos_python.json", "w") as f:
        json.dump(results, f, indent=2)
