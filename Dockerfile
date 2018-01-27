FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY jpsanford.conf /etc/nginx/conf.d/
EXPOSE 80 443