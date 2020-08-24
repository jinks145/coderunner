FROM frolvlad/alpine-gxx
RUN mkdir src
WORKDIR src
COPY ./fileStorage src
EXPOSE 3000
RUN cd src && ls
RUN apk add --no-cache g++
RUN /usr/bin/g++ src/runner.cpp -o runner
CMD ["./runner"]
