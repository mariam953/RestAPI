FROM python:3

ENV FLASK_APP "/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0