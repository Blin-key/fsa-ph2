FROM debian
RUN apt-get -y update && apt-get -y install python3-flask
WORKDIR /flask-docker
COPY health.py app.py 
EXPOSE 5000/tcp
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
