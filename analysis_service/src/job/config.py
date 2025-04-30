from pydantic_settings import BaseSettings


class JobConfig(BaseSettings):
    MODEL_NAME: str = "gemini-1.5-pro"


job_config = JobConfig()
