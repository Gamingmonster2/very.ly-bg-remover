from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove

app = FastAPI()

# إعداد الـ CORS لضمان اتصال الواجهة بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "my-secret-key-2026"

@app.post("/remove-bg")
async def remove_background(
    file: UploadFile = File(...), 
    x_api_key: str = Header(...)
):
    # 1. التحقق من مفتاح الـ API
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="مفتاح API غير صالح")
    
    # 2. قراءة ومعالجة الصورة
    input_image = await file.read()
    output_image = remove(input_image)
    
    # 3. إرجاع النتيجة
    return Response(content=output_image, media_type="image/png")
