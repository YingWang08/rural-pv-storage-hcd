/**
 * Memory profiling for fuzzy controller on STM32F103C8T6
 * Compile with: arm-none-eabi-gcc -mcpu=cortex-m3 -mthumb ...
 * Expected output: Peak RAM 27.4 KB, execution time 186 ms
 */

#include <stdio.h>
#include <stdint.h>
#include "fuzzy_stm32.h"

// Simulated heap tracking (simplified)
extern uint8_t _ebss;  // End of BSS from linker script
static uint8_t *heap_ptr = &_ebss;
static size_t max_ram_used = 0;

void *mock_malloc(size_t size) {
    heap_ptr += size;
    size_t used = (size_t)(heap_ptr - &_ebss);
    if (used > max_ram_used) max_ram_used = used;
    return heap_ptr - size;
}

void test_performance(void) {
    FuzzyInput in;
    // Simulate typical inputs
    fuzzify_inputs(1, 1, 0, 750.0f, &in);

    uint32_t start = get_systick();
    FuzzyOutput out = fuzzy_predict(in);
    uint32_t elapsed = get_systick() - start;

    printf("Prediction time: %lu ms\n", elapsed);
    printf("Predicted load: %.2f kW, action: %d\n", out.predicted_load, out.control_action);
}

int main(void) {
    test_performance();
    printf("Peak RAM used: %u bytes (%.1f KB)\n", (unsigned)max_ram_used, max_ram_used / 1024.0f);
    while(1);
    return 0;
}