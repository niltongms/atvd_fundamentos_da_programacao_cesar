arquivo = open("ips.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

print("IPs válidos:")
for ip in linhas:
    partes = ip.strip().split(".")
    if len(partes) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in partes):
        print(ip.strip())

print("\nIPs inválidos:")
for ip in linhas:
    partes = ip.strip().split(".")
    if not (len(partes) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in partes)):
        print(ip.strip())
