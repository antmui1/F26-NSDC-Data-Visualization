# F26-NSDC-Data-Visualization
Welcome! This is the GitHub repository for Anthony's F26 NSDC Data Visualization project, intended as a centralized place for you all to do work. GitHub is a platform that works with Git to host repositories in the cloud, and a repository is a place where code is stored. By creating a repo in GitHub, users are able to work collaboratively with others.

## To Begin
To begin, I would recommend creating some kind of folder on your computer for where you put code repositories. I have a Windows laptop, and I personally have my repos saved in `C:\Users\amui\source\repos`, but realistically, anywhere works. Alternatively, you can open PowerShell (for Windows) or Terminal (for macOS/Linux) and run 
```{bash}
cd ~
mkdir repos
```
to create a folder called repos in your home folder. Alternatively, you can run:
```{bash}
cd ~
mkdir -p source/repos
```
to create a folder called repos inside a folder called source in your home folder. Or if you want to name it differently, go for it. What's more important is that this folder exists and you remember where on your computer it is. 

For this next step, you're going to want to ensure that Git is installed and configured on your device. If you haven't, please look through [this website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for instructions, and also, I can help you during 1-1s or if you let me know separately. 

Next, you're going to want to clone this repo. Open PowerShell (for Windows) or Terminal (for macOS/Linux). If your repo folder is ~/repos, run:

```{bash}
cd ~/repos
git clone https://github.com/antmui1/F26-NSDC-Data-Visualization.git
```

If your repo folder is ~/source/repos, run:

```{bash}
cd ~/source/repos
git clone https://github.com/antmui1/F26-NSDC-Data-Visualization.git
```

If your repos folder is in a different place, then just replace `~/repos` or `~/source/repos` with the file path to your folder.

Assuming everything is configured, it should copy everything from this repo into a folder in your repos folder. 

Then open VSCode, make sure you have Python/VSCode set up, press open folder, and find the repos folder and specifically, the `~/repos/F26-NSDC-Data-Visualization` folder.
