Prerequisites

Make sure you have the following installed:

Docker (version 20.10 or later)

Python (for development and testing)

Building the Docker Image

To build the Docker image for the NLP API, follow these steps:

Clone this repository to your local machine.


git clone https://github.com/RupeshSangoju/GTM_Buddy/tree/master

cd GTM_Buddy

Build the Docker image using the following command:


docker build --no-cache -t nlp_api .

The --no-cache option ensures that Docker doesn’t use cached layers from previous builds.

The -t nlp_api flag tags the image with the name nlp_api.

Running the Docker Container

After building the image, you can run the container with this command:


docker run -p 5000:5000 nlp_api

This will run the nlp_api container and map port 5000 inside the container to port 5000 on your local machine.

The API will be accessible at http://127.0.0.1:5000.



Once the container is running, the API will expose the following endpoint:

POST /predict

Description: Accepts a text input and returns a prediction or processed result.

Request Body: JSON with a key text containing the input string.

Example:


{
  "text": "CompetitorX offers better pricing and a free trial. Our team is considering your AI engine for analytics."
}

Response: The processed result of the input text.

Example:


{
  "summary": "Your AI engine is being considered for analytics."
}


Troubleshooting


If you encounter issues with the docker build or docker run commands, ensure Docker is running and your terminal has the necessary permissions.

If there is an issue with missing dependencies, you may need to rebuild the Docker image or check your local environment.
