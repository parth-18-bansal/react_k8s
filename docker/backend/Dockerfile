FROM python:3.10-alpine

WORKDIR /app

COPY ../../backend/requirements.txt ./

RUN pip install -no-cache-dir -r requirements.txt

COPY ../../backend/app.py ./

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]