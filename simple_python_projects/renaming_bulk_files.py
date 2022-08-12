# Program that renames all the files in a particular folder


import os
# def main():
#     path = "C:\\Users\\Josephine P\\Desktop\\Pics\\"
#     i = 0

#     for filename in os.listdir(path):
#         print(path + "/" + filename)
#         original_name = path + filename
#         new_name = f"{path}img{i}.jpg"
#         print(new_name)
#         os.rename(original_name, new_name)
#         i += 1


# if __name__ == "__main__":
#     main()

# print("Done")

def main():
    path = "C:\\Users\\Josephine P\\Desktop\\Pics"
    i = 0

    try:
        for filename in os.listdir(path):
            # print(path + "/" + filename)
            original_name = path + filename
            new_name = f"{path}img{i}.jpg"
            # print(new_name)
            os.rename(original_name, new_name)
            i += 1
    except FileNotFoundError:
        print("File not found")
        # print(f)


if __name__ == "__main__":
    main()

print("Done")
