FROM python:3.11-slim

USER root

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
  apt-get install -y mariadb-server && \
  pip install --no-cache-dir -r requirements.txt && \
  rm -rf /var/lib/apt/lists/* && \
  mkdir -p /run/mysqld && chown mysql:mysql /run/mysqld

COPY . .

# Variáveis de ambiente (pode sobrescrever no docker run)
ENV DB_USER=rafael
ENV DB_PASS=aptdw
ENV DB_NAME=mydb

EXPOSE 3306 8000

CMD mysqld --user=mysql --datadir=/var/lib/mysql --bind-address=0.0.0.0 & \
  sleep 10 && \
  mysql -u root -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};" && \
  mysql -u root -e "CREATE USER IF NOT EXISTS '${DB_USER}'@'%' IDENTIFIED BY '${DB_PASS}';" && \
  mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO '${DB_USER}'@'%' WITH GRANT OPTION;" && \
  mysql -u root -e "FLUSH PRIVILEGES;" && \
  uvicorn main:app --host 0.0.0.0 --port 8000