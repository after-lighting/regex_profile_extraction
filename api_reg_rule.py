from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from main import reg_search
from convert_docx_format import convert_docx_format

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message" : "Hello World!"}

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File()):
    await file.seek(0)
    contents = await file.read()
    upload_path = "upload_file.docx"
    with open(upload_path, "wb") as f_out:
        f_out.write(contents)
    formatted_message_item_list = convert_docx_format(upload_path)
    reg_result = reg_search(formatted_message_item_list)
    return {"reg_result": reg_result}

# uvicorn api_reg_rule:app --reload