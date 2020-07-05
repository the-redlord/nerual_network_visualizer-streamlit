FROM python:3.8-slim-buster
RUN adduser -D net
WORKDIR /app
# RUN apk add linux-headers
# RUN apk add --update python3-dev build-base
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
COPY start.sh ./
RUN chmod +x start.sh

RUN chown -R net:net ./
USER net

EXPOSE 8501
# CMD ["gunicorn", "-b :5000", "ml_server:app"]
ENTRYPOINT ["./start.sh"]