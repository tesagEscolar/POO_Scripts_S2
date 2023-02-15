!/bin/bash
# lines that start like this are shell comments
# read projects current directory with $PWD

cd $PWD
git add .
git commit -am “$commitMessage”
git push
exit 1