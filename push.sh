#!/usr/bin/env bash

#just to quicken the pushing process
#to use this file, run
# ./push.sh "my commit message"
#eg ./push.sh "did the first task"

COMMIT_MESSAGE=$1

if [ ! "$COMMIT_MESSAGE" ];
then
echo "No commit message found"
echo "Run ./push 'your commit message' "
echo "Aborting..."
echo "Your changes were not published"
else
echo "Adding to repository..."
git add -A
echo "Commiting the latest changes"
git commit -m COMMIT_MESSAGE
echo "Pushing to remote..."
git push
echo "++++++++++++++++++++++++++++++++++++"
echo "Changes published to remote with the message $COMMIT_MESSAGE"
echo "++++++++++++++++++++++++++++++++++++"
fi