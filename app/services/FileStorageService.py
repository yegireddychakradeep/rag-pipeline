import os
import uuid

from fastapi import Path, UploadFile

from app.uploadStrategy.UploadStrategy import UploadStrategy



class FileStorageService():
    def __init__(self,strategy : UploadStrategy, file : UploadFile):
        self.__file = file
        self.__strategy = strategy


    async def store_to_disk(self):
        await self.__strategy.uploadFile(self.__file)
        
        
    






