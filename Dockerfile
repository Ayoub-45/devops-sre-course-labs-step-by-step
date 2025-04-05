FROM python:3.7-slim

WORKDIR /app

ADD . /app

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8090

# execute the Flask app
ENTRYPOINT ["python"]
HEALTHCHECK CMD curl --fail http://localhost:8090/ || exit 1
CMD ["/app/app.py"]
