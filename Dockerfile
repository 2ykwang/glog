FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .

# ENV ALLOWED_HOSTS 127.0.0.1
ENV PORT 8000

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
  
CMD python manage.py collectstatic