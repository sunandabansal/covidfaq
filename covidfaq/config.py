from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    elastic_search_host: str = "faq-master"
    elastic_search_port: int = 9200

    class Config:
        env_prefix = ""
        case_insensitive = True


@lru_cache()
def get() -> Config:
    return Config()
