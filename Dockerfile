FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# copying all files over
COPY . /app

# Expose port 
ENV PORT 5000

CMD ["python", "app.py"]
