# Custom processing block example (C++)

This is an example of a custom processing block, which you can load in the Edge Impulse studio. See the docs: [Building custom processing blocks](https://docs.edgeimpulse.com/docs/custom-blocks). The features in this block are implemented in C++, then exposed to Python using pybind11. The Python code spins up a web server, which Edge Impulse then talks to.

## C++ Bindings

The [library](library) folder contains a C++ library ([cpp/test.hpp](library/cpp/test.hpp)) with Python bindings ([py/eicpp.cpp](library/py/eicpp.cpp)). To test it out quickly (verified on macOS):

1. Install [pybind11](https://pybind11.readthedocs.io/en/stable/installing.html) and a recent version of CMake.
2. Build the library:

    ```
    sh library/build-library.sh
    ```

3. Run the example:

    ```
    python3 library/py/test.py
    ```

## Running the block locally (Docker)

1. Build and run the container:

    ```
    docker build -t custom-block-cpp . && \
        docker run --rm -it -v $PWD/server:/app/server -p 4446:4446 custom-block-cpp
    ```

2. To add the block to Edge Impulse, see [Exposing the processing block to the outside world](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/custom-blocks#exposing-the-processing-block-to-the-world).

## Hosting the block in Edge Impulse

See [Hosting custom DSP blocks](https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/custom-blocks/hosting-custom-dsp-block).
