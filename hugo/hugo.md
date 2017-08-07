Hugo
open-source static site generator

Blistering Speed
빠른 속도

Robust Content Management

Shortcodes
단순한 Markdown

Built-in Templates
SEO, commenting, analytics 사전제작 템플릿을 제공

Multilingual and i18n
다국어 i18n지원

Custom Outputs
JSON, AMP, multiple format custom output 지원

Hugo Theme 지원
https://themes.gohugo.io
https://gohugo.io/templates/

## Install Hugo
https://gohugo.io/getting-started/installing/
brew doctor
brew update
brew install hugo

which hugo
show the location of the hugo executable

ls -l $( which hugo )
show the installed version

hugo version
verify that hugo runs correctly

hugo help

tree
archetypes
	content define
	default tags or categories and define types such as a post, tutorial or product
	

config.toml
	main configuration 
	define all of the websites title
	language
	urls
	etc
	
content
	content pages of the site
	
data
	localization configuration
	
layouts
	layouts for the Go html/template library
	
static
	any static files
	any css, js or image file
	
themes
	create new themes or clone themes from github


hugo new site {create site name}
cd {create site name}

hugo new post/first-post.md
writing content in first-post.md by editor
hugo new privacy.md

hugo server
hugo server -w -D

curl -L localhost:1313/privacy/


##Hugo Themes
https://github.com/gohugoio/hugoThemes
Installing all Themes
	git clone --depth 1 --recursive https://github.com/gohugoio/hugoThemes.git themes
Installing a single theme
	cd themes
	git clone URL_TO_THEME
	
hugo server -t {themename}





## reference urls
https://www.slideshare.net/MarcinGajda/hugo-make-webdev-fun-again
https://libsora.so/posts/migration-from-pelican-to-hugo-post-mortem/
https://blog.funspaces.org/2016/02/15/hugo-hyde-y-theme/
https://blog.funspaces.org/2016/02/16/automated-deployments-with-wercker/
http://brannpark.github.io/blog/posts/20151201_hugo_with_github_pages/
http://kerberosj.tistory.com/216
http://sabzil.org/hugo/
https://blog.leehack.com/blog/2015/11/25/hugo-설치하기/
https://golangkorea.github.io/post/hugo-intro/getting-started/
http://credenda.blog.me/220574167327
https://code.tutsplus.com/tutorials/make-creating-websites-fun-again-with-hugo-the-static-website-generator-written-in-go--cms-27319

