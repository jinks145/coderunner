FROM FROM python:3.6-alpine

RUN adduser -D coderunner
#set working dir
WORKDIR home/experiment
#copies coderunner source code from the original working dir
COPY coderunner coderunner
COPY migrations migrations
#install pipenv
RUN pip install pipenv
# install Pipfile and dependencies
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
#run pipenv install to create a pipenv from the dependency
RUN pipenv install


RUN chmod +x boot.sh




EXPOSE 8000
ENTRYPOINT ["./boot.sh"]