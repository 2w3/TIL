https://www.docker.com/community-edition  
https://store.docker.com/editions/community/docker-ce-server-ubuntu  
https://docs.docker.com/install/linux/docker-ce/ubuntu/  

uninstall old versions  
```
$ sudo apt-get remove docker docker-engine docker.io
```

install docker ce  
install using the repository  
set up the repository  
```
$ sudo apt-get update
```
```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
$ sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```    
install docker ce  
```
$ sudo apt-get update
```
```
$ sudo apt-get install docker-ce
```
```
$ apt-cache madison docker-ce

docker-ce | 17.12.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
```
```
$ sudo apt-get install docker-ce=<VERSION>
```
```
$ sudo docker run hello-world
```
```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
# reboot or re-login
sudo service docker restart
```
