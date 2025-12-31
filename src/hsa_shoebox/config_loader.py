import yaml
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_config():
    """Loads configuration from the root config.yaml file."""
    # Locates the config file relative to this script's location
    config_path = Path(__file__).parent.parent.parent / "config.yaml"
    
    if not config_path.exists():
        logger.error(f"Configuration file not found at {config_path}")
        raise FileNotFoundError(f"Missing config.yaml at {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    mode = config.get("data_mode", "sample")
    input_path = Path(config["paths"][mode])
    output_path = Path(config["paths"]["output"])
    
    logger.info(f"Configuration loaded. Mode: {mode} | Input: {input_path}")
    return input_path, output_path