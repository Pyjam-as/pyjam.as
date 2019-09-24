
FROM python:3.7-slim-stretch

# install deps
RUN pip install pipenv
WORKDIR /tmp
COPY ./Pipfile* ./
RUN pipenv install --system --deploy

# copy in app
WORKDIR /
COPY ./pyjamas /pyjamas

# run shit
CMD hypercorn --bind 0.0.0.0:80 'pyjamas:create_app()'
