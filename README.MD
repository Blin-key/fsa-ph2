how to run:
#create network:
docker network create --driver bridge --opt com.docker.network.bridge.enable_icc=true netginx
#build and run the webserver:
docker build ./nginx/ -t webbie/server && docker run --name webbie -d --network=netginx webbie/server
#build and run the proxieserver:
docker build ./xnign/ -t proxie/server && docker run --name proxie -d --network=netginx -p 80:80 -p 443:443 proxie/server 


resources used:
- https://www.baeldung.com/linux/nginx-docker-container
- https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
- https://medium.com/insiderengineering/docker-networking-enabling-communication-between-containers-09c1ac1cf2dc

