#!/bin/sh

setup_git() {
  git config --global user.email ${EMAIL}
  git config --global user.name ${NAME}
}

commit_files() {
  cp README.md docs/
  git add . *.md
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin https://${GH_TOKEN}@github.com/hurcy/awesome-ehr-deeplearning.git > /dev/null 2>&1
  git push --quiet --set-upstream origin master 
}

setup_git
commit_files
upload_files