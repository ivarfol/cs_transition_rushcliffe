#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:49:57 2024

@author: iaroslav
"""
from enum import Enum
from os import path
from typing import Tuple, Type

from pydantic import Field, conint
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)
class YesNoEnum(str, Enum):
    YES = "yes"
    NO = "no"
    
def get_config_file():
    config_file = path.join(path.abspath(path.dirname(__file__)), 'guessing_game.yaml')
    if not path.isfile(config_file):
        raise ValueError(
            f"Config file ({config_file}) is missing"
        )
    return config_file

class Settings(BaseSettings, case_sensitive=True):
    model_config = SettingsConfigDict(yaml_file=get_config_file())
    ask_wordle: YesNoEnum = Field(YesNoEnum.NO)
    wordle: YesNoEnum = Field(YesNoEnum.YES)
    simultaneous: YesNoEnum = Field(YesNoEnum.NO)
    simultaneous_num: conint(ge=1, le=10) = Field(default=1)
    ask_tries: YesNoEnum = Field(YesNoEnum.YES)
    tries: conint(ge=5, le=20) = Field(default=5)
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, dotenv_settings, YamlConfigSettingsSource(settings_cls)
    
def get_settings() -> Settings:
    if get_config_file():
        return Settings()  # type: ignore
    else:
        raise FileNotFoundError("Config directory not found")
        
