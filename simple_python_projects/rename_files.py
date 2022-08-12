import os

path = "C:/Users/Josephine P/Downloads/Compressed Certs"

# for filename in os.listdir(path):
#     # print(filename)
#     if "_compressed" in filename:
#         # print(filename)
#         os.rename(f"{path}/{filename}", f"{path}/{filename.replace('_compressed', '')}")
    
#     print(filename)

for filename in os.listdir(path):
    # print(filename)
    
    base = os.path.basename(f"{path}/{filename}")
    # print(base)
    split_txt = os.path.splitext(base)
    print(split_txt)
    
    os.rename(f"{path}/{filename}", f"{path}/{split_txt[0]}")
    # if "_compressed" in filename:
    #     # print(filename)
    #     os.rename(f"{path}/{filename}", f"{path}/{filename.replace('_compressed', '')}")
    
    # print(filename)