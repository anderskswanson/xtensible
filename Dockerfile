FROM python:3.6

ENV APP_HOME /xtensible-bot
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME/
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt
