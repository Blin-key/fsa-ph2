FROM debian
RUN apt-get -y update && apt-get -y install nginx
COPY nginxconf /etc/nginx/sites-available/default 
EXPOSE 80/tcp
# nginx kan binnen de container "op de voorgrond" draaien;
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
