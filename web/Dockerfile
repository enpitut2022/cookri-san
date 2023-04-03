FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
RUN apt-get update && apt-get install -y curl 
RUN service nginx start

EXPOSE 80