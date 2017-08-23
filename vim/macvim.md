MacVim
http://macvim-dev.github.io/macvim/
https://github.com/macvim-dev/macvim/blob/master/README_vim.md

MacVim을 사용하는걸로
vim의 경우 멀티바이트 언어를 지원하지 않아
한글을 편집하려고 하면 화면이 깨져 나온다.
MacVim을 사용하면 멀티바이트 언어를 지원해주기 때문에
한글편집에도 문제가 없다.

기본적으로 gvim이 포팅된 형태이고 
OS X의 키보드 숏컷 바인딩 지원
자체적으로 python, perl, ruby 인터프리터를 포함할 수 있기때문에
vim을 빠져나오지 않고도 python, ruby등의 스크립트를 수행하거나 바로 디버깅이 가능하다.

Install MacVim
https://nolboo.kim/blog/2016/09/16/vim-8-upgrade/
brew install macvim --override-system-vim
brew linkapps

mv /usr/local/bin/vim /usr/local/bin/vim8
mv /usr/local/bin/vimdiff /usr/local/bin/vimdiff8
mv /usr/local/bin/vimtutor /usr/local/bin/vimtutor8
ln -s /usr/local/bin/vim8 /usr/local/bin/vi8

mvim -v 터미널안에서 mvim이 실행된다
mvim mvim이 독립된 응용프로그램으로 실행된다

MacVim 한글
http://seorenn.blogspot.kr/2011/04/vim-macvim.html
https://nolboo.kim/blog/2016/11/07/vim-korean/
https://withrails.com/2009/12/13/macvim-한글설명/
http://daybreaker.tistory.com/630


macvim clipboard sharing
~/.vimrc
```set clipboard=unnamed```
http://vim.wikia.com/wiki/Mac_OS_X_clipboard_sharing



http://seorenn.blogspot.kr/2011/06/vim-macvim.html
http://blog.mitsuha.me/2017/02/06/macvim-install-failed-issue/
http://popfly.egloos.com/6080434
http://seohakim.blogspot.kr/2015/02/mac-vim.html



