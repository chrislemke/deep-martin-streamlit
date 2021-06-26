#!/bin/bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install transformers==4.6.1 streamlit==0.82.0 pandas==1.2.4 numpy==1.19.5 openpyxl==3.0.7 torch==1.9.0
sudo yum install tmux


cd app
#tmux new -s streamlit
export STREAMLIT_SERVER_PORT=80
streamlit run main.py
#tmux attach -t streamlit