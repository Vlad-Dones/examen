FROM python:3.9.14-alpine3.16
USER root
COPY . .
RUN apk update && pip install --upgrade pip && pip install requests
ENTRYPOINT ["python", "test_exam.py"]