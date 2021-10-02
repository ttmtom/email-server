FROM python:3.8-slim-buster AS builder

WORKDIR /usr/src/app/
COPY ./ ./
RUN pip install pipenv

RUN pipenv install

FROM builder AS email-server-dev
CMD [ "pipenv", "run", "flask", "run", "--reload", "--debugger", "--host", "0.0.0.0"]
