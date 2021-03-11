# 1. Simple directory tree

import os

os.mkdir(r"C:\draft_code")

os.mkdir(r"C:\draft_code\pending")

os.mkdir(r"C:\draft_code\complete")

os.mkdir(r"C:\includes")

os.mkdir(r"C:\layouts")

os.mkdir(r"C:\layouts\default")

os.mkdir(r"C:\layouts\post")

os.mkdir(r"C:/layouts/post/posted")

os.mkdir(r"C:/site")

os.rmdir(r"C:\draft_code\pending")

os.rmdir(r"C:\draft_code\complete")

os.rmdir(r"C:\draft_code")

os.rmdir(r"C:\includes")

os.rmdir(r"C:/layouts/post/posted")

os.rmdir(r"C:\layouts\default")

os.rmdir(r"C:\layouts\post")

os.rmdir(r"C:\layouts")

os.rmdir(r"C:/site")

#Feedback - technically this is correct, again a lot of manual work done to create these folder trees.

import os


root_path = r"C:\Empty"
os.mkdir(root_path)


first_level = ["draft_code", "includes", "layouts", "site"]

for folder in first_level:

    os.mkdir(os.path.join(root_path, folder))

second_level = ["pending", "complete"]

for folder in second_level:

    os.mkdir(os.path.join(root_path, "draft_code", folder))


os.mkdir(os.path.join(root_path, "layouts", "default"))
os.mkdir(os.path.join(root_path, "layouts", "post"))
os.mkdir(os.path.join(root_path, "layouts", "post", "posted"))


import shutil
shutil.rmtree(root_path)
