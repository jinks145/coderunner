# Docker for the sibling image
FROM gcc:10.2.0
RUN mkdir src
WORKDIR src
COPY ./fileStorage src
EXPOSE 5000
RUN cd src && ls
RUN g++ src/runner.cpp -o runner
CMD ["./runner"]
