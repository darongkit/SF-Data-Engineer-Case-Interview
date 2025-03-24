Building the postgresql database:
navigate to dir with tableScript and Dockerfile
1 - build the docker image with dockerfile - docker build -t section2_postgres_image .
2 - docker run --name section2_postgres_container -p 5432:5432 -d section2_postgres_image
