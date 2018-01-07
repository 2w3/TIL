https://github.com/brave/browser-laptop/blob/master/docs/linuxInstall.md#debian-jessie-and-ubuntu-zesty-yakkety-xenial-and-trusty-amd64


```
curl https://s3-us-west-2.amazonaws.com/brave-apt/keys.asc | sudo apt-key add -  
echo "deb [arch=amd64] https://s3-us-west-2.amazonaws.com/brave-apt `lsb_release -sc` main" | sudo tee -a /etc/apt/sources.list.d/brave-`lsb_release -sc`.list
```

sudo apt update
sudo apt install brave
