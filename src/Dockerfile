FROM python:3.11-slim-bullseye
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt &&\
    flake8 . --select W293,E501,E302,E303
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]
