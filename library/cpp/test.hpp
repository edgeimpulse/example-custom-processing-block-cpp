#pragma once

#include <float.h>
#include <vector>
#include <iostream>
#include <numeric>

namespace ei {

float min(const std::vector<float>& in_data) {
    float min = FLT_MAX;
    for (auto v : in_data) {
        if (v < min) {
            min = v;
        }
    }
    return min;
}
float max(const std::vector<float>& in_data) {
    float max = -FLT_MAX;
    for (auto v : in_data) {
        if (v > max) {
            max = v;
        }
    }
    return max;
}
float avg(const std::vector<float>& in_data) {
    float sum = 0.0f;
    for (auto v : in_data) {
        sum += v;
    }
    return sum / in_data.size();
}

}
