import os
path = 'tekst.txt'
# print(os.stat(path))
if os.stat(path).st_size > 0:
    print("File not empty")
else:
    print("Empty file")
# -----
# if os.path.exists(path) and os.stat(path).st_size > 0:
#     print("Be careful")
# else:
#     print("Ok")
# -----