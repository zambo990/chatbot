FROM python:3.9

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y cmake

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "main.py"]
