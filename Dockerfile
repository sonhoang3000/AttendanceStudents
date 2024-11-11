FROM python:3.12-alpine

# Install CMake và các gói khác để sử dụng building wheel for dlib 
RUN apt-get update && apt-get install -y \
      build-essential \
      cmake \
      libgl1-mesa-glx \
      libglib2.0-0 \
      && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./app /app

RUN pip install --upgrade pip
RUN pip install -r requirement.txt

EXPOSE 5000

CMD ["python", "webapp.py"]