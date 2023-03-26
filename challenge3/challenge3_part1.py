# Replicate this tree of directories and subdirectories:

# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.

import os

os.mkdir(r"D:\draft_code")
os.mkdir(r"D:\draft_code\pending")
os.mkdir(r"D:\draft_code\complete")

os.mkdir(r"D:\includes")

os.mkdir(r"D:\layouts")
os.mkdir(r"D:\layouts\default")
os.mkdir(r"D:\layouts\post")
os.mkdir(r"D:\layouts\post\posted")

os.mkdir(r"D:\site")


os.removedirs(r"D:\draft_code\pending")
os.removedirs(r"D:\draft_code\complete")


os.rmdir(r"D:\includes")

os.removedirs(r"D:\layouts\post\posted")
os.removedirs(r"D:\layouts\default")

os.rmdir(r"D:\site")