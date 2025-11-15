from abc import ABC, abstractmethod
from typing import List

from anonymous_board.entity.anonymous_board import AnonymousBoard


class AnonymousBoardRepository(ABC):

    @abstractmethod
    def create(self, title: str, content: str) -> AnonymousBoard:
        pass

    @abstractmethod
    def find_all(self) -> List[AnonymousBoard]:
        pass

    @abstractmethod
    def read_by_id(self, board_uuid: str):
        pass
