FROM python:3.7-alpine
MAINTAINER Neil Guan & Block Chen 2019/11/08
WORKDIR /usr/src/app
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/bin/sh", "-c", "python -u ./app.py"]
