# Python 이미지 사용
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt .
RUN pip install -r requirements.txt

# FastAPI 코드 복사
COPY . /app

# FastAPI 실행 -->쿠버네티스에서 쓰기 좋음
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5173"]
