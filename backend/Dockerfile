# Base Python image
FROM tiangolo/uvicorn-gunicorn:python3.9

EXPOSE 80

COPY src src
COPY setup.cfg setup.cfg
COPY setup.py setup.py


# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -e .[all]

# Health check
HEALTHCHECK CMD curl --fail http://localhost:80/status || exit 1

# Run API server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "info"]
