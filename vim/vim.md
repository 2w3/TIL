Vim
is a highly configurable text editor built to make creating and changing any kind of text very efficient.
It is an improved version of the vi editor distributed with most UNIX systems.

Vi IMproved

vim learning curve 가파르다.
Emacs는 변태용
숙달되면 그 어떤 에디터보다 생산성이 빠르다.


Modal Editor
ex Mode
:
Normal(Command) Mode
Esc
Insert Mode
i
Visual Mode
v

ctrl +v block selection

저장과 종료
:w(write)
:q(quit)
:wq(write and quit)
:q!(quit without writing)
ZZ write and quit
ZQ quit without writing

주로 쓰는 것들
dw 단어 삭제
dd 라인 삭제
3dd 3라인 삭제
10, 13d 10라인에서 13라인까지 삭제
gg 맨 첫 줄로
G 맨 끝 줄로
>, < 들여쓰기 한 칸 넣기, 한칸 빼기
u 실행
y 복사
yy 줄 복사
p 붙여넣기
= 들여쓰기 자동 정렬

5gg 맨 위에서 5칸 아래로 커서 이동
5dd 5줄 삭제
5 > 5줄 1칸 들여쓰기
gg=G 처음부터 끝까지 다시 자동 들여쓰기

:set nu 라인 넘버
:set ai 엔터 후 들여쓰기
:colorscheme(scheme name) 컬러스킴 설정
:syntax on 문법 강조 키기
:set ts=4 탭 사이즈 4로
:set autoindent 자동 들여쓰기 키기
:set smartindent 자동 들여쓰기 키기
:set shiftwidth=4 자동 들여쓰기 간격 4로

:o filename open filename
:sh 콘솔로 다시 넘어감, exit치면 다시 vi로 돌아옴
:!+console command 콘솔 명령어 실행
:!ls
:r!+console command 콘솔 명령어 실행후 출력을 vi에 삽입
:tabnew 새로운 탭 열기
:tabs 탭들 목록 보여주기

Color Scheme
syntax highlight
/colors 아래 color schem.vim파일을 넣으면 됨

http://colorswat.ch/vim
http://vimcolors.com

.vimrc
vim 설정파일
:set, :colorscheme 설정
set t_Co=256 256색
set xterm-256color 256색
colorscheme {color scheme name} 
set nu=number 줄 번호
set ai=auto indent 엔터후 들여쓰기
set tabstop=4 tab을 4 space로 설정
set shiftwidth=2 >>나 << 사용시 들여쓰기 간격지정
set softtabstop=2 탭 간격을 공백문자로 변환하면 삭제할때 탭 간격만큼 삭제하기 않고, 마치 탭 문자를 삭제한것처럼 설정하며, 두칸 단위로 삭제
set visualbell 사용자 실수를 경고할때 비프음 대신 화면 번쩍임으로 경고
set syntax on 구문 강고 기능을 사용
set background=dark 배경색을 어두운 색으로 설정
set backspace=eol, start, ident 줄의 끝, 시작, 들여쓰기에서 백스페이스를 사용하면 이전줄과 연결
set history=100 편집기록 100개까지 기억
set ignorecase 검색, 편집, 치환시에 대소문자 구분 없앰
set showmatch {}, ()에서 닫는 괄호입력할때 일치하는 괄호 보여줌
set showmode 현재 mode보여주기
set listchars

Ubuntu 기본 tiny Vim에서는 몇가지 설정이 적용안됨

Plugins
https://gibbon.co/pinda/guide-to-vim
http://vimawesome.com

Vim Commands Cheat Sheet
https://www.fprintf.net/vimCheatSheet.html
https://vim.rtorr.com/lang/ko/


설치
MacVim을 사용하는걸로
vim의 경우 멀티바이트 언어를 지원하지 않아
한글을 편집하려고 하면 화면이 깨져 나온다.
MacVim을 사용하면 멀티바이트 언어를 지원해주기 때문에
한글편집에도 문제가 없다.
brew install macvim --override-system-vim


Plugin
.vimrc

Vundle
Plugin Manager
플러그인 관리자
https://github.com/VundleVim/Vundle.vim
Vundle은 git으로 download 받아서 사용

Vundle 설치, 설정
http://luckyyowu.tistory.com/308
http://dreamlog.tistory.com/79
https://ansuchan.com/install-vundle-and-nerdtree/
https://github.com/uyu423/vimrc-vundle-script
https://github.com/VundleVim/Vundle.vim

Esc키를 Caps Lock키로 매핑해서 사용

YCM(youcompleteme)
http://neverapple88.tistory.com/26
SuperTab보다 낫다

The NERD Tree (Cmd + K, B)
디렉토리 탐색기
https://github.com/scrooloose/nerdtree
Search File (Cmd + P)
Automatically Complete Word
Multiple Cursor
Monokai Theme
https://github.com/crusoexia/vim-monokai

ctrlp.vim
파일명으로 파일 찾기
https://github.com/kien/ctrlp.vim

AutoComplPop
https://github.com/vim-scripts/AutoComplPop

vim-multiple-cursors
refactoring을 쉽게 해준다.
https://github.com/terryma/vim-multiple-cursors

http://iamabluetiger.com/vim-review/

BufExplorer

less

ctags

tag explorer

auto-pairs

emmet-vim

vimshell.vim

Ack.vim

fugitive.vim
vim와 git을 통합
https://github.com/tpope/vim-fugitive
Git Support 



seoul256.vim

seoul256.vim is a low-contrast Vim color scheme based on Seoul Colors. Works on 256-color terminal or on GVim.

https://github.com/junegunn/seoul256.vim


reference urls
https://www.joinc.co.kr/w/Site/Vim/Documents/UsedVim
https://robots.thoughtbot.com/the-vim-learning-curve-is-a-myth
https://nolboo.kim/blog/2016/11/15/vim-for-beginner/
http://www.openvim.com/tutorial.html
https://www.sitepoint.com/getting-started-vim/
http://www.mimul.com/pebble/default/2014/07/15/1405420918073.html
https://vim-adventures.com
http://vimdoc.sourceforge.net
https://www.slideshare.net/benjaminhkoh/vim-48710063

read later
http://riseshia.github.io/2016/09/12/vim-2-months.html
http://heeraenae.tistory.com/entry/OS-XLinuxUbuntu-C-C-개발-환경-구축
https://github.com/nelstrom/vim-markdown-preview
https://ansuchan.com/install-vundle-and-nerdtree/
https://www.slideshare.net/benjaminhkoh/vim-48710063
https://nolboo.kim/blog/2017/03/05/grok-vi/?utm_source=weirdmeetup&utm_medium=original_link_on_post&utm_campaign=vi를+진정으로+이해해라
https://nolboo.kim/blog/2016/10/13/vim-text-objects-definitive-guide/?utm_source=weirdmeetup&utm_medium=original_link_on_post&utm_campaign=Vim+텍스트+개체%3A+궁극의+가이드
https://nolboo.kim/blog/2016/09/19/vim-visula-mode-block-export-import/?utm_source=weirdmeetup&utm_medium=original_link_on_post&utm_campaign=Vim의+비주얼+모드와+텍스트+블록+저장과+파일+임포트
https://nolboo.kim/blog/2016/09/20/vim-plugin-manager-vundle/?utm_source=weirdmeetup&utm_medium=original_link_on_post&utm_campaign=Vim의+플러그인+관리자+Vundle과+플러그인+설치
http://blog.weirdx.io/?s=vim
http://jungcool.tistory.com/44
https://medium.com/@mjkim111/vim-첫-걸음-떼기-ae0138290ae0
http://vimcasts.org
http://ohyecloudy.com/pnotes/archives/1799/
http://seorenn.blogspot.kr/2011/06/vim-macvim.html
http://blog.doortts.com/139
http://cafe.daum.net/_c21_/bbs_search_read?grpid=c1Sx&fldid=LrFJ&datanum=82&q=%B4%D9%C0%BD%C7%C3%B7%AF%B1%D7%C0%CE%BC%B3%C4%A1&_referer=V7kfJwkeLEGMZxGlgqZEmWvUOwI6AXsXxysQCBUmhh5k85LxPn6Umx73ZJGk-XmJhdbWFlbtfg5rIKXLIUSjn61_AGqjH68p
http://webkebi.zany.kr:9003/board/bView.asp?bCode=13&aCode=2289
https://github.com/dokenzy/vimrc
https://blog.zzolab.com/pretty-vim/
http://berrybox.com/?p=29
https://www.eunchan.kim/workflow.html


external usb esc key
https://www.google.co.kr/search?client=safari&rls=en&biw=1342&bih=990&tbm=isch&sa=1&q=external+usb+esc+key&oq=external+esc+key+&gs_l=psy-ab.3.1.0i30k1j0i8i30k1j0i5i30k1l2.4812.11977.0.14654.22.22.0.0.0.0.232.2540.0j16j1.17.0....0...1.1j4.64.psy-ab..5.15.2287.0..0j0i19k1j0i30i19k1.id3Ou2MLJGo