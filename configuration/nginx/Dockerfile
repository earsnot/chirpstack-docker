FROM nginx:1.21.5-alpine
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./conf/proxy_params /etc/nginx/proxy_params
RUN mkdir /etc/nginx/sites-enabled
COPY ./conf/default.conf /etc/nginx/sites-enabled/default.conf
RUN mkdir /etc/nginx/certs/
COPY ./certs/ /etc/nginx/certs/