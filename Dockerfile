FROM python:3.11

WORKDIR /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install spacy separately to avoid errors
RUN pip install spacy
RUN python -m spacy download en_core_web_sm

# Install other dependencies
RUN pip install -r requirements.txt

CMD ["python", "src/inference_service.py"]
