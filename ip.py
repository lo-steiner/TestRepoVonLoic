MyFile = open("Ip.txt", "w")


for a in range(256):
    for b in range(256):
        for c in range(256):
            for d in range(256):
                MyFile.write(f"{a}.{b}.{c}.{d}\n")
