FROM python:3.9

WORKDIR /the/workdir/path

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN export PYTHONPATH=.

COPY . .

EXPOSE 8000

CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8000"]


