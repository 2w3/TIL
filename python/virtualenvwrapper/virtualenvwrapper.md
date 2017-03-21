# install virtualenvwrapper
```
pip install virtualenvwrapper
```
`virtualenvwrapper` is toolkit that helps using virtualenv more pleasant.

# configure for virtualwrapper 
### 1. create virtualenv configuration directory
```
mkdir ~/workspace/.virtualenvs
```
### 2. create shell runtime configuration  
```
vim ~/.zshrc
```
### 3. write configration in shell runtime configuration
```
export WORKON_HOME=~/workspace/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
# create virtualenv in WORKON_HOME
```
mkvirtualenv {create virtualenv name}
```
New virtualenv is automatically activated after being initialized.
# create python3 virtualenv
```
mkvirtualenv {create virtualenv name} -python=pyton3
```

# activate virtualenv
```
workon {create virtualenv name}
```
# move another virtualenv
```
(current virtualenv)$ workon {another virtualenv}
```
# deactivate virtualenv
```
deactivate
```
# virtualenv list
```
lsvirtualenv
```
# remove virtualenv
```
rmvirtualenv {virtualenv name}
```
# reference url
[http://virtualenvwrapper.readthedocs.io/en/latest/](http://virtualenvwrapper.readthedocs.io/en/latest/)
