# Add project in git hub repository:
---------------------------------
>Configure local repository:
===========================
:Configure user_name , user_email and see all configre list
mds-MacBook-Pro:API-pytest-project mdrubel$ git config --global user.name "rubeldm123"
mds-MacBook-Pro:API-pytest-project mdrubel$ git config --global user.email "rubeldm123@gmail.com"
mds-MacBook-Pro:API-pytest-project mdrubel$ git config --list
credential.helper=osxkeychain
user.name=rubeldm123
user.email=rubeldm123@gmail.com
--------------------------------------------------------------------------------------
>Create local Repository:
===========================
:Create a Local repository in different location then project location example:create folder in desktop"
------
mds-MacBook-Pro:~ mdrubel$ cd Desktop
mds-MacBook-Pro:Desktop mdrubel$ mkdir Api_Automation_python_Jan2021
mds-MacBook-Pro:Desktop mdrubel$ cd Api_Automation_python_Jan2021/
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ pwd
/Users/mdrubel/Desktop/Api_Automation_python_Jan2021

::::::::git init:::::: Initiallize Local repositor with .git extention
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git init
Initialized empty Git repository in /Users/mdrubel/Desktop/Api_Automation_python_Jan2021/.git/
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ ls -all
total 0
drwxr-xr-x@  3 mdrubel  staff   96 Jan 23 13:46 .
drwx------@ 24 mdrubel  staff  768 Jan 23 13:46 ..
drwxr-xr-x@  9 mdrubel  staff  288 Jan 23 13:46 .git
:::::::::::::::::::::::::::::::::::::::::::::::::::


git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/rubeldm123/API_Automation_Python_Jan2021.git
git push -u origin main