import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "memory_test_size": 100,  # MB
    "cpu_test_duration": 5,   # seconds
    "disk_test_size": 50,     # MB
    "verbose": False
}

def load_config() -> Dict[str, Any]:
    """Load configuration from file or use defaults"""
    config_path = 'src/config.json'
    
    if os.path.exists(config_path):
        with open(config_path) as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return DEFAULT_CONFIG

def save_config(config: Dict[str, Any]):
    """Save configuration to file"""
    with open('src/config.json', 'w') as f:
        json.dump(config, f, indent=2)
