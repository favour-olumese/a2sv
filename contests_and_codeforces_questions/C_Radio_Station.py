n, m = input().split()

servers = {}
for _ in range(int(n)):
    server, ip = input().split()

    servers[ip] = server

for _ in range(int(m)):
    command, ip = input().split()
    print(f'{command} {ip} #{servers[ip[:-1]]}')