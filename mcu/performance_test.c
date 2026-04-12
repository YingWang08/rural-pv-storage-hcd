/**
 * Performance benchmark: fuzzy_predict() execution time.
 * Measures 1000 iterations and reports average.
 */

#include "fuzzy_stm32.h"
#include "stm32f1xx_hal.h"

#define ITERATIONS 1000

void performance_test(void) {
    FuzzyInput in;
    fuzzify_inputs(1, 2, 1, 400.0f, &in);

    uint32_t start = HAL_GetTick();
    for (int i = 0; i < ITERATIONS; i++) {
        FuzzyOutput out = fuzzy_predict(in);
        (void)out;
    }
    uint32_t elapsed = HAL_GetTick() - start;

    float avg_ms = (float)elapsed / ITERATIONS;
    printf("Average prediction time: %.2f ms\n", avg_ms);
}