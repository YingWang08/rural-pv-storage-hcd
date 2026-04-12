#ifndef FUZZY_STM32_H
#define FUZZY_STM32_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

#define LOAD_UNIVERSE_SIZE   51   // 0..5 kW step 0.1
#define ACTION_UNIVERSE_SIZE 4    // 0:charge,1:discharge,2:idle,3:reserve

typedef struct {
    float season_busy;
    float season_slack;
    float season_transition;
    float time_night;
    float time_morning;
    float time_midday;
    float time_evening;
    float farmer_ordinary;
    float farmer_planting;
    float farmer_aquaculture;
    float irrad_low;
    float irrad_medium;
    float irrad_high;
} FuzzyInput;

typedef struct {
    float predicted_load;   // kW
    int   control_action;   // 0-3
} FuzzyOutput;

// Main prediction function
FuzzyOutput fuzzy_predict(FuzzyInput input);

// Utility to fuzzify crisp inputs
void fuzzify_inputs(int season, int time_of_day, int farmer_type, float irradiance, FuzzyInput *out);

#ifdef __cplusplus
}
#endif

#endif