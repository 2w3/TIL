## submodule

submodule은 git repository안에 다른 git repository를 둘 수 있게 해준다.  
서로 다른 두개의 git repository 모두 독립적으로 관리할 수 있다.

submodule은 repository가 다른 project의 checkout을 directory형태로 저장 할 수 있도록 해준다.

submodule은 자신의 정체성을 유지  
submodule의 repository와 commit ID를 저장  
submodule을 포함한 상위 프로젝트("super projct")를 복사한 다른 개발자가 동일한 버전의 모든 submodule을 쉽게 복사할수 있도록 해준다  
super project의 일부분만을 checkout하는것이 가능하다  
git에게 submodule을 전혀 포함하지 않거나, 일부만 포함하거나, 모두 포함하도록 지정할 수 있다


git 하위폴더에 git을 하나 더 사용할 일이 생길 경우 사용하는 방법  
보통 submodule로 들어가는 git은 lib형태로 배포되는 소스일 경우가 많습니다

submodule을 사용하게 되면 함께 사용되는 두개의 프로젝트를 독립적으로 운영할 수 있다는 장점

하나의 repository가 또 다른 repository에 들어갈수 있다는 개념

외부 모듈을 참조

`git submodule` 명령을 이용해서 외부 모듈을 clone할 수 있다.  
`git submodule`은 같은 working directory에 여러 module을 추가할 수 있는 장점이 있다.

git submodule {sub command} {path} {name}

## git submodule을 만드는 방법

~~이미 생성되어 있는 git에서 submodule add을 실행~~  
`git submodule add`명령으로 프로젝트를 submodule로 추가한다.  
`git submodule add git://github.com/chneukirchen/rack.git rack`  
`rack` 디렉토리가 생성된다.  
이렇게 하면 현재 git폴더 아래에 subdir이라는 폴더가 생기고 그 안에 .git폴더가 생성됩니다.

~~git에서 git status를 실행하면 new file이 두개 생성되어 있습니다.~~  
`git status`명령을 실행하면 .gitmodules, rack 두개의 파일을 볼 수 있다.
```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#      new file:   .gitmodules
#      new file:   rack
#```

.gitmodules : 어떤 git module이 사용되고 있는지에 대한 정보를 저장하는 파일
```
$ cat .gitmodules
[submodule "rack"]
      path = rack
      url = git://github.com/chneukirchen/rack.git
```
local directory path와 project url의 mapping info가 저정된 설정파일이다.  
submodule 갯수만큼 이 항목이 생긴다.  
.gitmodules도 .gitignore파일처럼 버전관리된다.  
project clone하는 사람은 .gitmodules파일을 보고 어떤 submodule project가 있는지 알 수 있다.

rack : submodule add시 지정한 submodule folder
```
$ git diff --cached rack
diff --git a/rack b/rack
new file mode 160000
index 0000000..08d709f
--- /dev/null
+++ b/rack
@@ -0,0 +1 @@
+Subproject commit 08d709f78b8c5b0fbeb7821e37fa53e69afcf433
```
git은 rack 디렉토리를 submodule로 취급하기 때문에 파일들을 직접 추적하지 않고 커밋 하나만 저장한다.  
`rack` directory에서 수정을 하고 commit하면 다른 사람이 같은 환경을 만들 수 있도록 HEAD가 가리키는 commit이 super project에 저장된다.

master처럼 branch name같은 reference가 저장되는 것이 아니라 commit의 SHA-1 값이 저장된다.

super project도 commit해야 된다.
```
$ git commit -m 'first commit with submodule rack'
[master 0550271] first commit with submodule rack
 2 files changed, 4 insertions(+), 0 deletions(-)
 create mode 100644 .gitmodules
 create mode 160000 rack
```

`rack` directory의 mode는 160000이다.  
160000 mode는 일반적인 file이나 directory가 아니라는 의미다.

sub project의 last commit이 바뀔때마다 super project에 저장된 commit도 바꿔준다.  
`rack` directory를 별도의 project로 취급하기 때문에 모든 git command는 독립적으로 동작한다.
```
$ git log -1
commit 0550271328a0038865aad6331e620cd7238601bb
Author: Scott Chacon <schacon@gmail.com>
Date:   Thu Apr 9 09:03:56 2009 -0700

    first commit with submodule rack
$ cd rack/
$ git log -1
commit 08d709f78b8c5b0fbeb7821e37fa53e69afcf433
Author: Christian Neukirchen <chneukirchen@gmail.com>
Date:   Wed Mar 25 14:49:04 2009 +0100

    Document version change
```

## submodule이 있는 project clone
submodule을 사용하는 project를 clone하면 해당 submodule directory는 empty directory이다.
```
$ git clone git://github.com/schacon/myproject.git
Initialized empty Git repository in /opt/myproject/.git/
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (6/6), done.
$ cd myproject
$ ls -l
total 8
-rw-r--r--  1 schacon  admin   3 Apr  9 09:11 README
drwxr-xr-x  2 schacon  admin  68 Apr  9 09:11 rack
$ ls rack/
$
```
`rack` directory가 있지만 비워져 있다.  

`git submodule init` 명령어로 submodule을 초기화하고  
`git submodule update` 명령으로 서버에서 데이터를 가져온다.  
데이터를 전부 가져오면 super proejct에 저장된 commit으로 checkout된다.  
```
$ git submodule init
Submodule 'rack' (git://github.com/chneukirchen/rack.git) registered for path 'rack'
$ git submodule update
Initialized empty Git repository in /opt/myproject/rack/.git/
remote: Counting objects: 3181, done.
remote: Compressing objects: 100% (1534/1534), done.
remote: Total 3181 (delta 1951), reused 2623 (delta 1603)
Receiving objects: 100% (3181/3181), 675.42 KiB | 173 KiB/s, done.
Resolving deltas: 100% (1951/1951), done.
Submodule path 'rack': checked out '08d709f78b8c5b0fbeb7821e37fa53e69afcf433'
```

git submodule add git@mygithost:billboard lib billboard  
`git submodule add`  
submodule을 추가하는 git 명령어  
`git@mygithost:billboard`  
submodule로 지정할 repository  
repository에서 submodule을 지원하는지 확인해야 한다  
`lib/billboard`  
submodule repository에 추가될 경로를 지정  


`.gitmodules`  
submodule에 대한 정보를 담고 있다  

`cat .gitmodules`
```
[submodule "lib/billboard"]

path = lib/billboard

url = git@mygithost:billboard
```


## submodule의 update 방법
```
git submodule init
git submodule update
```
누군가 submodule을 수정하고 난 후에는 git pull이나 repo sync후  
항상 git submodule update 명령으로 submodule을 update 해주어야 합니다.

그렇지 않으면 git은 sync가 된 상황인데도 git status명령에 변화가 있는 상태로 표시가 됩니다.

## submodule 실제 사용방법
만들어진 subdir 아래에서 몇개의 commit변화가 발생하였을 경우
다른 곳에서 submodule을 포함한 git에 git clone / repo sync를 하고나면
현재 git은 *깨끗한 상태가 아닌 것*으로 표시됩니다.

이럴때 현재 해당사항을 commit하여 현재 git에 push하여 주어야 합니다.
그러면 git log에 subdir에 대한 변경사항이 update되어 다른 곳에서 sync를 하여도 동일한 내용을 볼 수 있게 됩니다.

다른 사람이 submodule을 변경한 것을 안다면 해당 사항을 merge하여 push하여도 됩니다.


git submodule add <repository> [path]  
path는 생략가능하고, 생략시 repository 이름과 동일한 디렉토리를 사용한다.

git repository 하위 sub git repository 관리하기 위함

parent.git  
git@github.com:{userid}/parent.git

하위 child.git  
git@github.com:{userid}/child.git

git submodule foreach  
http://manywaypark.tistory.com/263


reference urls  
~~http://bluelight.tistory.com/566~~  
~~http://bestend.co.kr/283~~  
~~http://javaworld.co.kr/44~~  
~~http://blog.powerumc.kr/449~~  
~~http://nving.tistory.com/68~~  
~~http://darkblitz.tistory.com/346~~  
~~http://mobicon.tistory.com/371~~  
~~http://www.sangkle.com/archives/71~~  
~~https://davidwalsh.name/git-remove-submodule~~  
~~https://gist.github.com/kyleturner/1563153~~  
~~https://git.wiki.kernel.org/index.php/GitSubmoduleTutorial~~  
~~https://forum.freecodecamp.org/t/how-to-remove-a-submodule-in-git/13228~~  
~~https://chrisjean.com/git-submodules-adding-using-removing-and-updating/~~  
~~http://ihacker.egloos.com/1274394~~  
~~http://youmin3.egloos.com/2104668~~  
https://git-scm.com/book/ko/v2/Git-도구-서브모듈
