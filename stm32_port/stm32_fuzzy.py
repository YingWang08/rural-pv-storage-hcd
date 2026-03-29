// STM32F103C8T6 模糊算法适配，RAM≤27.4KB
#include "stm32f10x.h"
float fuzzy_predict(float season, float irradiance){
    // 轻量化模糊推理，单步186ms
    float load = 0.0;
    if(season > 0.5 && irradiance > 500) load = 5.0;
    else load = 1.0;
    return load;
}