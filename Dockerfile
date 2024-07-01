# syntax = docker/dockerfile:experimental
FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# python3, pip and pybind11
RUN apt update && apt install -y python3 python3-pip python3-pybind11 wget

# Cmake
COPY ./build-dependencies/install_cmake.sh install_cmake.sh
RUN bash install_cmake.sh && \
    rm install_cmake.sh

# Update pip
RUN pip3 install -U pip==22.0.3

# Rest of the dependencies
COPY requirements-blocks.txt ./
RUN pip3 --no-cache-dir install -r requirements-blocks.txt

# C++ lib
COPY library/ library/
RUN bash library/build-library.sh

COPY . ./

EXPOSE 4446

ENTRYPOINT ["python3", "-u", "server/dsp-server.py"]
