git config --global user.email "you@example.com"  
git config --global user.name "Your Name"
ssh-keygen -C ‘your@email.address’ -t rsa
cat /c/user/999/.ssh/github.pub


Github web: Settings -- SSH ang GPG keys -- New SSH key -- Add SSH key

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
 
