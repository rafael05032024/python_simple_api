import paramiko

host = "172.18.0.1"
port = 22
username = "root"
pwd = "12345678"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def exec_ssh_command():
    try:
        client.connect(host, port, username, pwd)

        print("✅ Conexão SSH estabelecida!")

        stdin, stdout, stderr = client.exec_command("ls -la")

        print(stdout.read().decode())
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client.close()
