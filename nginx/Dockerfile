FROM debian
RUN apt-get -y update && apt-get -y install nginx
COPY nginxconf /etc/nginx/sites-available/default
COPY ai_story.html /usr/share/nginx/html/index.html 
EXPOSE 8080/tcp
# nginx kan binnen de container "op de voorgrond" draaien;
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
