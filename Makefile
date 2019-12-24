# Uz docker image s: https://gist.github.com/tkrajina/1b12fcc6c48fb3e582ac803a9f517146
pdflatex_cmd=docker run -v $(shell pwd):/latex -it latex pdflatex
build:
	$(pdflatex_cmd) pznp.tex