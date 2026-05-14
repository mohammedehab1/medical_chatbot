from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  
    )

    APP_NAME: str
    APP_VERSION: str

    GROQ_API_KEY: str
    LLM_MODEL: str

    WHISPER_MODEL: str

    TTS_VOICES_EN: str
    TTS_VOICES_AR: str

    AUDIO_INPUT_PATH: str
    AUDIO_OUTPUT_PATH: str

    TEMPERATURE: float = 0.3
    MAX_RETRIES: int = 2

    HF_TOKEN: str 
    BASE_MODEL_ID: str 
    FINETUNE_MODEL: str

settings = Settings()