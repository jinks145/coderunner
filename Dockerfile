FROM frolvlad/alpine-gxx
RUN mkdir src
WORKDIR src
COPY ./coderunner/fileStorage src
EXPOSE 3000
RUN cd src && ls
RUN apk add --no-cache g++
RUN /usr/bin/g++ src/test.cpp -o test
CMD ["./test"]
