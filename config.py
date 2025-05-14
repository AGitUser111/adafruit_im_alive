from getpass import getpass

from pydantic import AliasChoices, Field, SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings, cli_parse_args=True, cli_kebab_case=True):
    """
    These values can also be set in a .env file.
    Place the .env file in the same directory as this script.
    """

    model_config = {
        "env_file": ".env",
    }

    ADAFRUIT_IO_USERNAME: str = Field(
        default_factory=lambda: input("Adafruit IO username: "),
        validation_alias=AliasChoices("ADAFRUIT_IO_USERNAME", "u"),
        description="Adafruit IO username",
    )
    ADAFRUIT_IO_KEY: SecretStr = Field(
        default_factory=lambda: getpass("Adafruit IO key: "),
        validation_alias=AliasChoices("ADAFRUIT_IO_KEY", "k"),
        description="Adafruit IO key",
    )
    SEND_INTERVAL_SECONDS: int = Field(
        default=10,
        validation_alias=AliasChoices("SEND_INTERVAL_SECONDS", "i", "interval"),
        description="Interval in seconds to send data. Must be greater than 1 on paid plan or greater than 2 on free plan.",
        min=1,
    )
    FEED_NAME: str = Field(
        default="uptime",
        validation_alias=AliasChoices("FEED_NAME", "f"),
        description="Feed name to send data to.",
    )


config = Config()
