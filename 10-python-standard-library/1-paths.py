# https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# Windows
Path("C:\\Program Files\\Microsoft")
# raw path
Path(r"C:\Program Files\Microsoft")

# linux or mac
Path('/usr/local/bin')

# from present folder
Path('1-paths.py')
# same as
Path() / "1-paths.py"

# get home directory of user
home = Path.home()
print(home)


# Useful properties and methods
path = Path('1-paths.py')
print(path.exists())
print(path.is_file())
print(path.is_dir())
# Absolute path
print(path.absolute())

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# This file actually doesn't exits, just returning a non existent path
# Dont know how this could be more useful
path = path.with_name('1-pathsEdited.py')
print(path)
