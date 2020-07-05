FROM python:3.8-alpine
RUN adduser -D net
WORKDIR /app

COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install wheel setuptools
COPY src/ /app
COPY start.sh ./
RUN chmod +x start.sh

RUN chown -R net:net ./
USER net

EXPOSE 8501
# CMD ["gunicorn", "-b :5000", "ml_server:app"]
ENTRYPOINT ["./start.sh"]