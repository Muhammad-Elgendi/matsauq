# pull official base image
FROM python:3.9.4-alpine3.12

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# create the app user
RUN addgroup -S app && adduser -S app -G app

# set work directory
WORKDIR /usr/src/app

# copy entrypoint.sh
COPY ./entrypoint.sh ../

# chown all the files to the app user
RUN chown -R app:app ./

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]