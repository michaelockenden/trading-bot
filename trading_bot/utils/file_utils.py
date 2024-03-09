from pathlib import Path

from environs import Env


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def get_env():
    env = Env()
    return env.read_env()
