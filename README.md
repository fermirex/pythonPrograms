git config --global user.email "**@outlook.com"
git config --global user.name "test"
ssh-keygen -t rsa -C "**@outlook.com" 

cat ./ssh/id_rsa

Github web: Settings -- SSH ang GPG keys -- New SSH key -- Add SSH key
Note:
 ssh -T git@github.com  #Test the connection with github
 ssh -v git@github.com  #Mode detail about the connection
 git always find id_rsa file as the ssh key, please rename the key generate above to id_rsa and put in the .ssh

cd ~/Desktop/filename
git init
git add.
git commit -m "===="

git remote add origin https://github.com/yourname/filename.git
git remote add origin git@github.com:yourname/filename.git

git push -u origin master

git push origin master (2nd and then ignor -u option)

2. How to ignore files in git
 a). Create .gitignore file in the git folder
 b). /mtk/ ignore ./mtk and it subfolder
 c) *.zip ignore all zip file
 d) /mtk/do.c ignore /mtk/do.c
 e) !*.zip not ignore zip file
 
