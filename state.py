from typing import Any
from storage import BaseStorage, JsonFileStorage

class State:
    """Класс для работы с состояниями."""

    def __init__(self, storage: BaseStorage) -> None:
        self.storage = storage

    def set_state(self, key: str, value: Any) -> None:
        """Установить состояние для определённого ключа."""
        state = self.storage.retrieve_state()
        state[key] = value
        self.storage.save_state(state)
        
    def get_state(self, key: str) -> Any:
        """Получить состояние по определённому ключу."""
        state = self.storage.retrieve_state()
        val = state[key] if key in state else None
        return val
    
    @property
    def isEmpty(self): return len(self.storage.retrieve_state()) < 1
