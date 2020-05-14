# Instructions

## Using pip

```bash
############ GENERAL NOTES ###############
# python3 instead of python
# to install stuff for python interpreter
# pip is basically npm or yarn I guess
# --user otherwise permission error

# 1) Upgrade pip
python3 -m pip install --upgrade pip --user

# 2) Install something like pylint
python3 -m pip install pylint --user
```

## VS code settings

I had to do this manually when I forgot to click yes on the pop about enabling pylint
Clicked yes on the autocomplete one, if not add that too I guess

[Useful Link](https://ruddra.com/posts/vs-code-for-python-development/#using-pep8-and-lint)

```json
{
	"python.pythonPath": "/usr/local/bin/python3",
	"python.linting.pylintEnabled": true
}
```
