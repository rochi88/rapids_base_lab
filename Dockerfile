# Use the RapidsAI base image
FROM rapidsai/base:24.06-cuda12.2-py3.10

USER root

# Install additional Python packages using pip
RUN pip install numpy pandas matplotlib scikit-learn bdshare gunicorn flask arctic

COPY src/ .

EXPOSE 5000

# Development
# CMD ["python3", "app.py"]

# Production
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]
