FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ./files /usr/src/app/files

ENTRYPOINT ["/bin/bash", "-c", "python ./app.py"]