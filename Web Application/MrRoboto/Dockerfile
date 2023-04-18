FROM nginx:1.23.1

# Copy config file
COPY roboto.conf /etc/nginx/conf.d/default.conf

# Copy nginx static source files
COPY ./404.html /usr/share/nginx/html/
COPY ./index.html /usr/share/nginx/html/
COPY ./robots.txt /usr/share/nginx/html/
COPY ./flag.txt /usr/share/nginx/html/4183a6fa/

EXPOSE 8080
ENTRYPOINT nginx -g 'daemon off;'
