FROM python:3.8.5-alpine3.12

RUN adduser -D coderunner
#set working dir
WORKDIR home/experiment

# install docker
RUN apk add docker

RUN addgroup coderunner docker
RUN adduser coderunner docker

# install docker-compose 
RUN apk add docker-compose

#copies coderunner source code from the original working dir
COPY coderunner coderunner
COPY migrations migrations

#install pipenv
RUN pip install pipenv
# install Pipfile and dependencies
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
#run pipenv install to create a pipenv from the dependency
RUN pipenv install --system
COPY boot.sh docker-compose.yml ./

RUN chmod +x boot.sh

ENV FLASK_APP coderunner.py

RUN chown -R coderunner:coderunner ./
# USER coderunner



EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
CMD ["/bin/sh"]
