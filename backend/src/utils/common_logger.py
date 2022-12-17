import os
import uvicorn
import logging

logging_level = os.environ.get("LOG_LEVEL", "INFO")
logging.basicConfig(
    level=logging_level,
    datefmt="%Y-%m-%dT%H:%M",
    format="[%(asctime)s.%(msecs)03dZ]: %(levelname)s: [%(module)s - L%(lineno)d] %(message)s",
)

LOGGER = logging.getLogger("safety_map")

# Create uvicorn error handler config
format_string = "[%(asctime)s.%(msecs)03dZ]:  - %(levelname)s - %(message)s"
uvicorn_log_config = uvicorn.config.LOGGING_CONFIG
uvicorn_log_config["formatters"]["access"]["fmt"] = format_string
uvicorn_log_config["formatters"]["default"]["fmt"] = format_string

# Handle uvicorn logger for the docker execution
logger = logging.getLogger("gunicorn.error")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(format_string))
LOGGER.addHandler(handler)
