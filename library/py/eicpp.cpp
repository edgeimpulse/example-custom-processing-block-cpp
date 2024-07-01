
#include <vector>
#include <string.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "../cpp/test.hpp"

namespace py = pybind11;

PYBIND11_MODULE(eicpp, m) {
    m.doc() = "Edge Impulse CPP Test";
    m.def("min", [](const std::vector<float>& in_data) {
        return ei::min(in_data);
    });
    m.def("max", [](const std::vector<float>& in_data) {
        return ei::max(in_data);
    });
    m.def("avg", [](const std::vector<float>& in_data) {
        return ei::avg(in_data);
    });
}
