from abc import ABC, abstractmethod


# ABC = Abstract Class
# Java : interface AnonymousBoardService { } 형태로 표현
# Rust : trait AnonymousBoardService
class AnonymousBoardService(ABC):

    @abstractmethod
    def create(self, title: str, content: str):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def read(self, board_id: str):
        pass
