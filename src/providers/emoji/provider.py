import random
from src.providers.base import BaseProvider
from src.providers.emoji.utils import get_time_of_day, time_of_day_emojis
from datetime import datetime


class EmojiProvider(BaseProvider):
    def __init__(self):
        ...

    def get(self) -> str:
        return self._get_emoji()

    def _get_emoji(self) -> str:
        time_of_day = get_time_of_day(datetime.now())

        emoji = time_of_day_emojis.get(time_of_day)

        if isinstance(emoji, list):
            return random.choice(emoji)
        if isinstance(emoji, str):
            return emoji
        else:
            raise ValueError("Unexpected type for emoji: " + type(emoji))
