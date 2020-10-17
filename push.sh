#! /bin/bash

read -p 'Push Message ? ' message

echo "Build ......"
cd frontend && yarn build:stage && cd ..
echo "Build finished"

git add . 
git commit . -m "$message"
git push origin master

echo "Push Success"%  
