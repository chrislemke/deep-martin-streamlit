FROM python:3.9.5-slim

WORKDIR /usr/app/src
RUN chown -R /usr/app/src 

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app ./

CMD ["sh", "-c", "streamlit run --server.port 8080 /usr/app/src/main.py"]