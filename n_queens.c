#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int count = 0;

int is_safe(int *board, int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col || abs(board[i] - col) == abs(i - row))
            return 0;
    }
    return 1;
}

void solve(int *board, int row, int n) {
    if (row == n) {
        count++;
        return;
    }
    for (int col = 0; col < n; col++) {
        if (is_safe(board, row, col)) {
            board[row] = col;
            solve(board, row + 1, n);
            board[row] = -1;
        }
    }
}

int solve_nqueens(int n) {
    count = 0;
    int *board = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) board[i] = -1;
    solve(board, 0, n);
    free(board);
    return count;
}

double now_ms() {
    return (double)clock() * 1000.0 / CLOCKS_PER_SEC;
}

int main() {
    int sizes[] = {4, 6, 8, 10, 12, 14, 15};
    int reps = 15;
    for (int s = 0; s < 7; s++) {
        int n = sizes[s];
        printf("Testando %dx%d...\n", n, n);
        double times[reps];
        for (int r = 0; r < reps; r++) {
            double t0 = now_ms();
            solve_nqueens(n);
            double t1 = now_ms();
            times[r] = t1 - t0;
        }
        double sum = 0, sum2 = 0;
        for (int i = 0; i < reps; i++) {
            sum += times[i];
            sum2 += times[i]*times[i];
        }
        double mean = sum / reps;
        double std = sqrt(sum2 / reps - mean*mean);
        printf("%dx%d: %.2f ± %.2f ms\n", n, n, mean, std);
    }
    return 0;
}
