# zsh 설치
```
brew update
brew install zsh
```

# 설치 확인
```
cat /etc/shells
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
```
# system shell로 변경
```
sudo chsh -s "$(command -v zsh)" "${USER}"
```
# oh-my-zsh 설치
```
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
# oh-my-zsh theme 수정
```
vim ~/.zshrc
#ZSH_THME="robbyrussell"
ZSH_THME="random"
```
# powerline font 설치
```
git clone https://github.com/powerline/fonts.git 
cd fonts 
./install.sh
```
