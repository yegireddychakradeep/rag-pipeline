from fastapi import APIRouter, UploadFile

from app.services.FileStorageService import FileStorageService
from app.uploadStrategy.SaveToDisk import SaveToDisk
router = APIRouter()

@router.post("/uploadPdf" , tags=["File uploads"])
async def upload_pdf(file : UploadFile):
    save_to_disk = SaveToDisk()
    storage_service = FileStorageService(save_to_disk, file)
    await storage_service.store_to_disk()
    return {"message" : "uploaded successfully"}


    
    