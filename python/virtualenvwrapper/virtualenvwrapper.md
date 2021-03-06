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
# create python2 virtualenv
```
mkvirtualenv {create virtualenv name} --python='which python'
```
# create python3 virtualenv
```
mkvirtualenv {create virtualenv name} --python='which python3'
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
[https://bitbucket.org/dhellmann/virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper)
[http://virtualenvwrapper.readthedocs.io/en/latest/install.html#quick-start](http://virtualenvwrapper.readthedocs.io/en/latest/install.html#quick-start)
[http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html](http://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
[http://virtualenvwrapper.readthedocs.io/en/latest/](http://virtualenvwrapper.readthedocs.io/en/latest/)
