FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=section2DB

# Copy the SQL script to the Docker image
COPY tableScript.sql /docker-entrypoint-initdb.d/

# Expose default PostgreSQL port
EXPOSE 5432