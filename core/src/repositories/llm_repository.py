from abc import ABC, abstractmethod


class AIAssistantRepository(ABC):
    @abstractmethod
    def create_thread(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_assistant(self, assistant_name: str):
        raise NotImplementedError

    @abstractmethod
    def add_message(self, thread_id: str, role: str, message: str):
        raise NotImplementedError
    
    @abstractmethod
    def create_and_poll(self, thread_id: str, assistant_id: str):
        raise NotImplementedError

    @abstractmethod
    def list_messages(self, thread_id: str):
        raise NotImplementedError
