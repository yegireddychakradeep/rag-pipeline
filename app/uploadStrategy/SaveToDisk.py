import asyncio
import os
import uuid

from fastapi import UploadFile
from pathlib import Path
from app.uploadStrategy.UploadStrategy import UploadStrategy


class SaveToDisk(UploadStrategy):
    async def uploadFile(self, file : UploadFile ):
    # 1. Fetch the path from environment variables
        storage_folder = os.environ.get("DIR_PATH","./uploads")
        target_folder = Path(storage_folder)

    # Ensure the directory exists on your storage drive  
        target_folder.mkdir(parents=True, exist_ok=True)

    # 2. Generate a highly unique system UUID
        file_uuid = str(uuid.uuid4())

        file_name = f"{file_uuid}-{file.filename}"
        destination_path = target_folder / file_name
        
        try:   
            with open(destination_path , "ab") as buffer :
                # file is fastapi 's UploadFile  already has thread offloading written in it 
                while chunk := await file.read(1024 * 1024):
                    await asyncio.to_thread( buffer.write,chunk )
            
        except(Exception) as e :

            print("error while saving to sdd", e )

        # cleanup fastapi temporary file  
        finally:
            await file.close()

                


        
        


         

