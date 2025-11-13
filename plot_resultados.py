import matplotlib.pyplot as plt


python_results = [(4, 0.06), (6, 0.65), (8, 13.59), (10, 359.05), (12, 8716.02)]
c_results = [(4, 0.00), (6, 0.00), (8, 0.10), (10, 6.05), (12, 149.80)]

plt.figure()
plt.plot([n for n, _ in python_results],
         [t for _, t in python_results], marker='o', label='Python')
plt.plot([n for n, _ in c_results],
         [t for _, t in c_results], marker='s', label='C')
plt.xlabel('Tamanho do tabuleiro (n)')
plt.ylabel('Tempo médio (ms)')
plt.yscale('log')
plt.title('Desempenho - Problema das N Rainhas (Backtracking)')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
