
run:
	. ./.env && \
	pipenv run \
	quart run


DOCKERIMG="pyjamas"
docker-build:
	docker build . -t $(DOCKERIMG)

docker-run:
	docker run -p 5000:80 $(DOCKERIMG)
