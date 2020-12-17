pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
make publish
cd output
git add .
git commit -m "$1"
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "$1"
git push -u origin master