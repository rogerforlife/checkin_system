FROM node:14.18.1 as build

LABEL maintainer xxxx@xxxxx.com
ENV NODE_ENV=production
ARG PROJECT_PATH=./react
ARG ENV=.env

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ${PROJECT_PATH}/package.json ${PROJECT_PATH}/yarn.lock ./
RUN yarn --production
COPY ${PROJECT_PATH} .
COPY ./${ENV} .env
RUN yarn build

FROM nginx:latest
COPY --from=build /app/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
