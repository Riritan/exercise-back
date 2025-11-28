# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ✅ 이 줄이 꼭 필요해요!
app = FastAPI()

# (선택) CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 프론트 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Record(BaseModel):
    accuracy: float
    fail: int
    success: int
    repeat: int
    user_id: str

@app.post("/record")
async def receive_record(data: Record):
    print("===== 새 요청 들어옴 =====")
    print(f"user_id : {data.user_id}")
    print(f"accuracy: {data.accuracy}")
    print(f"success : {data.success}")
    print(f"fail    : {data.fail}")
    print(f"repeat  : {data.repeat}")
    print("=========================")
    return {"status": "ok", "message": "data received"}