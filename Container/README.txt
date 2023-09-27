Flight App Docker Container Deployment Guide
--------------------------------------------

This document provides a step-by-step guide on how to deploy and run the Flight App container from the provided tar archive.

Pre-requisites:
---------------
- A computer with Docker installed.

Instructions:
-------------

1. **Load the Docker Image**:
   
   First, ensure you are in the directory containing the `flight_app.tar` file. Then, load the Docker image from the tar archive:

docker load -i flight_app.tar


Once completed, the `flight_app:latest` image will be available on your machine.

2. **Run the Docker Container**:

Depending on the nature of the Flight App, you'll adjust the run command accordingly. If, for instance, the app is a web application running on port 8000, you'd use:

docker run -p 8000:8000 flight_app:latest


The `-p 8000:8000` maps port 8000 inside the container to port 8000 on your machine. Adjust the port mappings if your application uses a different port.

3. **Access the Application**:

If the Flight App is a web application, open a browser and navigate to:

http://localhost:8000


If the app uses a different port, adjust the URL accordingly.

4. **Check the Container's Status and Logs**:

To see a list of running containers:

docker ps

For logs related to the Flight App:

docker logs <container_id_or_name>

Thank you for using the Flight App. If you encounter any issues, please refer to the main project documentation or contact the development team.






