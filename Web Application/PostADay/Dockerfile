FROM node:latest

WORKDIR /home/
COPY ./src /home/

RUN npm install

ENV FLAG=CHAD{E@T-th0se_4PplEs!!}
ENV PORT=4545

EXPOSE 4545
ENTRYPOINT node index.js
