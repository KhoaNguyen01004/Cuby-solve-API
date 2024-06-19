# Dockerizing and Running Your Application
This guide will walk you through the steps to Dockerize and run your Python Flask application.

## Prerequisites
- Docker installed on your machine
- Your application code

## Steps
### 1. Build the Docker Image
To build the Docker image, navigate to the directory containing your Dockerfile and run the following command:
```bash
docker build --tag cube-solve-api .
```
This command builds a Docker image using the Dockerfile in the current directory and tags it as Cube-solve-API.

### 2. Run the Docker Container
After the image has been built, you can run it as a container with the following command:
```bash
docker run -p 5000:5000 cube-solve-api
```
This command runs the Docker container and maps port 5000 inside the container to port 5000 on your host machine.  

### 3. Access the Application
Once the Docker container is running, you can access your application at http://localhost:5000. 