FROM python:3.8

COPY oar /app/oar
COPY scrapy.cfg /app
COPY poetry.lock /app
COPY pyproject.toml /app

WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN $HOME/.poetry/bin/poetry install --no-dev

CMD $HOME/.poetry/bin/poetry run scrapy crawl secure.sos.state.or.us
