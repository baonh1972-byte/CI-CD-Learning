# 1. Dùng một hệ điều hành siêu nhẹ có sẵn Python
FROM python:3.9-slim

# 2. Tạo một thư mục làm việc bên trong Container
WORKDIR /app

# 3. Copy toàn bộ file từ máy bạn vào trong Container
COPY . .

# 4. Chạy các bài Test ngay khi đóng gói (Để đảm bảo thùng này sạch lỗi)
RUN python -m unittest discover test

# 5. Lệnh mặc định khi khởi động Container (chạy một file bất kỳ)
CMD ["python", "calculator.py"]
