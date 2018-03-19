#!/bin/bash

jupyter-nbconvert --to slides KNNfromScratchSlides.ipynb --reveal-prefix=reveal.js
git add .
mv KNNfromScratchSlides.slides.html index.html
git add .
git commit -m "new version"
git push origin gh-pages