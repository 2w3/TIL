Zsh
Z shell
is a Unix shell that can be used as an interactive login shell and as a powerful command interpreter for shell scripting.
Zsh is extened Bourne shell with large number of improvements, including some features of Bash, ksh, and tsch.


Features
command-line completion
command history
file globbing
variable/array
editing of multi-line
spelling correction
various compatibility modes
themeable prompts
full TCP and Unix domain socket controls, an FTP client, and extended math functions


Zsh tip

What are the best UNIX shells?
https://www.slant.co/topics/513/~best-unix-shells


check info zsh
zsh --version

Install Zsh
brew install zsh

Use the brew zsh
sudo dscl . -create /Users/$USER UserShell /usr/local/bin/zsh
which zsh
zsh --version

Confirm Running Brew zsh
dscl . -read /Users/$USER UserShell
echo $SHELL

Set Shell in Iterm2
iTerm2 -> Preferences -> Profiles -> Default -> General -> Command
echo $SHELL

Handling Upgrades
sudo chown -R $(whoami):admin /usr/local

sudo vi /etc/shells
sudo chsh -s 'which zsh'
echo $SHELL


vi ~/.zshrc
export PATH=/usr/local/bin:$PATH


https://rick.cogley.info/post/use-homebrew-zsh-instead-of-the-osx-default/

https://blog.ayukawa.kr/archives/1758
