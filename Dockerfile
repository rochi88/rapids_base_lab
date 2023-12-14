# Use the RapidsAI base image
FROM rapidsai/base:23.12-cuda12.0-py3.10

# Install additional Python packages using pip
RUN pip install pandas matplotlib scikit-learn 

COPY src/main.py .

CMD ["python3", "main.py"]
