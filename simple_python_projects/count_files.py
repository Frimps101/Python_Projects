import os

# path = "C:/Users/Josephine P/Downloads/Compressed Certs"

path = "C:/Users/Josephine P/Downloads/Certificates 2"
count = 0

for filename in os.listdir(path):
    # print(filename)
    count += 1
    

print(count)