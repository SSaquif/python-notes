# Instructions

## Using pip

```bash
############ GENERAL NOTES ###############
# python3 instead of python to use python 3
# to install stuff for python interpreter
# pip is basically npm or yarn I guess
# --user otherwise permission error

# 1) Upgrade pip
python3 -m pip install --upgrade pip --user

# 2) Install something like pylint
python3 -m pip install pylint --user

## Running python CLI

# 1) python 2
python

# 2) python 3
python3
```

## VS code settings

I had to do this manually when I forgot to click yes on the pop about enabling pylint
Clicked yes on the autoPep one (its a formatter), if not add that too I guess. Note: it worked

[Useful Link](https://ruddra.com/posts/vs-code-for-python-development/#using-pep8-and-lint)

```json
{
	"python.pythonPath": "/usr/local/bin/python3",
	"python.linting.pylintEnabled": true
}
```
