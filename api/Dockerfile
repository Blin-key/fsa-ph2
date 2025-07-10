FROM debian
RUN apt-get -y update && apt-get -y install python3-flask curl
WORKDIR /flask-docker
COPY health.py app.py 
#EXPOSE 5000/tcp
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD curl --fail http://localhost:5000/api/health || exit 1
#HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD if [[ "$(curl -s http://localhost:5000/api/health)" =~ 'status: "ok"' ]]; then exit 0; else exit 1; fi
