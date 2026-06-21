from abc import ABC, abstractmethod

from fastapi import UploadFile


class UploadStrategy(ABC):
    @abstractmethod
    async def uploadFile(self , file : UploadFile):
        pass
