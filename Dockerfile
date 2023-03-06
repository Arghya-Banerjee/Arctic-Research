FROM python:3.9-slim-buster

WORKDIR /arcticResearch

COPY . /arcticResearch

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
