import os
from pathlib import Path

from environs import Env


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def get_env():
    env = Env()
    env.read_env()
    return os.environ["API_KEY"], os.environ["API_SECRET"]
