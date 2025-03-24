Building the postgresql database:
navigate to dir with tableScript and Dockerfile
1 - build the docker image with dockerfile - docker build -t section2_postgres_image .
2 - docker run --name section2_postgres_container -p 5432:5432 -d section2_postgres_image

once connected to the database using an IDE, I used DBeaver to connect to the PostgreSQL.
Simply open the script in the DB and execute the testdata and query scripts to replicate results.
