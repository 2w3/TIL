# check virtualenv path
```
which virtualenv
```

# install virtualenv
```
pip install virtualenv
```
# uprade virtualenv
```
pip install virtualenv --upgrade
```
# create virtualenv
```
virtualenv {create virtualenv name}
```
# activate virtualenv
```
source {create virtualenv name}/bin/activate
{create virtualenv name}$
```
# deactivate virtualenv
```
{create virtualenv name}$ deativate
```

# freeze current virtualenv packages
```
{create virtualenv name}$ pip freeze > package_list.txt
```
`package_list.txt` this file contains list of all packages in current environment, and their respective versions.
# re-create freeze virtualenv
```
{create other virtualenve name}$ pip install -r package_list.txt
```
# reference  
[https://pypi.python.org/pypi/virtualenv](https://pypi.python.org/pypi/virtualenv)
