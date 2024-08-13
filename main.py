from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles

api = FastAPI()
app = FastAPI()

@api.get("/baz")
async def baz_r():
    return { "message": "baz" }

@api.post("/upload")
async def accept_file_r(file: UploadFile):
    with open(f'data/{file.filename}', 'wb') as resultFile:
        resultFile.write(await file.read())
        resultFile.close()

    return { "message": "bar" }

app.mount("/api", api)
app.mount("/", StaticFiles(directory="static",html = True), name="static")
