FROM node:latest

WORKDIR /home/
COPY ./challenge /home/

RUN npm install

ENV FLAG=CHAD{S3cr3ts_C@n_B3_Fun!?!}
ENV IS_DOCKER=true
ENV ADMIN_PORT=4810
ENV CHALLENGE_PORT=5679

EXPOSE 5679

ENTRYPOINT node challenge.js
