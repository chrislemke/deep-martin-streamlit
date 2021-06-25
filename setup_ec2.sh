#!/bin/bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install transformers==4.6.1 streamlit==0.82.0 pandas==1.2.4 numpy==1.19.5 openpyxl==3.0.7 torch==1.9.0
cd app
streamlit run main.py