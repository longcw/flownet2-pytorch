#!/bin/bash
cd ./networks/correlation_package
python setup.py build_ext --inplace
cd ../resample2d_package 
python setup.py build_ext --inplace
cd ../channelnorm_package 
python setup.py build_ext --inplace
cd ..
