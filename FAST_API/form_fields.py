from fastapi import FastAPI, Form,File, UploadFile
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

# @app.post("/login/")
# async def login(user:User = Form() , password : str = Form):
#     return {"user":user , "password":password}

# request files--------------------------------

@app.post("/file/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file":file,"file_size": len(file) }

@app.post("/files/upload")
async def create_upload_file(file: UploadFile| None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
    
# UploadFile with Additional Metadata                                                    
@app.post("/uploadfile/")
async def upload_file_des(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}

# Multiple File Uploads

@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


# request forms and files-------------------
@app.post("/files2/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }