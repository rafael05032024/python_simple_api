FastAPI + MariaDB Kubernetes Setup

Este projeto demonstra como configurar uma aplicação FastAPI com MariaDB usando Kubernetes e Docker. Inclui exemplos de PVC e Deployment, além de dicas de desenvolvimento e testes.

Aprendizados:

- Instalar extensões para Python:
  - Black Formatter (formatação automática)
  - Flake8 (linting)
- Executar testes unitários:
  pytest -v
- Executar a aplicação localmente:
  docker-compose up

Persistent Volume Claim (PVC):

Arquivo pvc.yaml para criar o volume persistente do MariaDB:

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-mariadb-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi

Deployment do Container:

Arquivo deployment.yaml para criar o deployment do FastAPI + MariaDB:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fastapi-app
  template:
    metadata:
      labels:
        app: fastapi-app
    spec:
      containers:
        - name: fastapi-app
          image: sua-imagem:latest  # sua imagem que já contém MariaDB
          ports:
            - containerPort: 8000
            - containerPort: 3306
          env:
            - name: DB_USER
              value: rafael
            - name: DB_PASS
              value: aptdw
            - name: DB_NAME
              value: mydb
          volumeMounts:
            - name: mariadb-storage
              mountPath: /var/lib/mysql
      volumes:
        - name: mariadb-storage
          persistentVolumeClaim:
            claimName: app-mariadb-pvc

Como usar:

1. Construir a imagem Docker:
   docker build -t sua-imagem:latest .
2. Subir o PVC no Kubernetes:
   kubectl apply -f pvc.yaml
3. Criar o Deployment:
   kubectl apply -f deployment.yaml
4. Verificar os pods e status:
   kubectl get pods
5. Conectar no MariaDB usando DBeaver ou outro cliente, utilizando a porta exposta.

Links Úteis:

- FastAPI Documentation: https://fastapi.tiangolo.com/
- MariaDB Documentation: https://mariadb.com/kb/en/
- Kubernetes Documentation: https://kubernetes.io/docs/
- Docker Documentation: https://docs.docker.com/
