#ifdef __linux__
#define __declspec(v)

#include <stdio.h>
#include <stdlib.h>

extern "C"{
    __declspec(dllexport) float interpolateNewton(float *x, float *y, int n, float t)
    {
        int    i, j;
        float c[100];
        float w[100];
        float sum;

        for (i = 0; i < n; i++) {
            w[i] = y[i];
            for (j = i - 1; j >= 0; j--)
                w[j] = (w[j+1] - w[j]) / (x[i] - x[j]);
            c[i] = w[0];
        }

        sum = c[n-1];
        for (i = n - 2; i >= 0; i--)
            sum = sum * (t - x[i]) + c[i];

        return sum;
    }
}
#endif
