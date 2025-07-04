FROM debian
RUN apt-get -y update && apt-get -y install nginx curl
COPY nginxconf /etc/nginx/sites-available/default
COPY ai_story.html /usr/share/nginx/html/index.html 
EXPOSE 8080/tcp
# nginx kan binnen de container "op de voorgrond" draaien;
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD curl --fail http://localhost:8080 || exit 1
