FROM node:lts-alpine as build-stage

WORKDIR /app
COPY yarn.lock .
COPY package.json .

RUN yarn --prod --frozen-lockfile
COPY . .
RUN yarn build


FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080


