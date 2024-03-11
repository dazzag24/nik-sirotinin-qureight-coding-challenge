import asyncio
from random import randrange
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # "http://localhost:5173",
    "*"
]

app.add_middleware(CORSMiddleware, 
                    allow_origins=origins,
                    #allow_methods=["OPTIONS", "PUT"],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"]
                )

@app.put("/isthisacat/")
async def isthisacat(file: UploadFile):
    if file.content_type != "image/jpeg":
        raise HTTPException(status_code=400, detail="Wrong file format")

    await asyncio.sleep(60)
    confidence = randrange(100)
    success = confidence > 50
    info = "Probably a cat" if success else "Doesn't look like a cat"

    return dict(success=success, confidence=confidence, info=info)
