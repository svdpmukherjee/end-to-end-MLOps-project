import os
import logging

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    handlers=[
        logging.FileHandler(os.path.join(log_dir, "running_logs.log")),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

