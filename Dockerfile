FROM node:lts-alpine as build-stage

WORKDIR /app
COPY yarn.lock .
COPY package.json .

RUN yarn --prod --frozen-lockfile
COPY . .
EXPOSE 8080


