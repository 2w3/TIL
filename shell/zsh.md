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
# 현재 shell 확인
```
echo $SHELL
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
# font 설치 확인
```
echo "\ue0b0 \u00b1 \ue0a0 \u27a6 \u2718 \u26a1 \u2699"
```
# iterm powerline font 설정
iterm에서 command + ,  
Profiles - Text - Font - Change Font - Use a different font for non-ASCII text - Change Font

![iterm powerline font configration](https://raw.githubusercontent.com/2w3/TIL/master/shell/capture_iterm_powerlinefont_configuration.png)


# zsh themes references

zsh2000  
![zsh2000 image]
(https://raw.githubusercontent.com/maverick9000/zsh2000/master/demo.png)
[https://github.com/maverick9000/zsh2000]
(https://github.com/maverick9000/zsh2000)

agnoster  
![agnoster image]
(https://gist.githubusercontent.com/agnoster/3712874/raw/screenshot.png)
[https://github.com/agnoster/agnoster-zsh-theme]
(https://github.com/agnoster/agnoster-zsh-theme)


# Why zsh is Cooloer than Your Shell
[https://www.slideshare.net/brendon_jag/why-zsh-is-cooler-than-your-shell]
(https://www.slideshare.net/brendon_jag/why-zsh-is-cooler-than-your-shell)