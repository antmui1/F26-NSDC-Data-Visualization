# Git Workflow Guide

This guide walks through contributing to this project: pull the latest changes, create a branch, make commits, push your branch, and open a pull request (PR).

Before starting, make sure you've followed the setup instructions in [README.md](README.md) and opened the `F26-NSDC-Data-Visualization` folder in VS Code. Ensure Git is installed and you have a GitHub account. 

## 1. Pull the latest changes from origin

`origin` is the name Git gives the GitHub repository when you clone it. Pulling brings changes from GitHub into your local copy.

1. Before starting a new task, make sure that you have all saved changes committed in a branch. If you're starting from fresh, you do not need to worry about this. 
2. Click the current branch name in the **bottom-left corner** of VS Code and select **main**.
3. Press the button in the bottom left that has an X, a number next to it, a warning sign, and another number next to it. This should open up a menu at the bottom of your screen. Press terminal. (Alternatively, select Terminal > New Terminal on the top.)
4. Run:

   ```bash
   git status
   ```

   Confirm it says `On branch main` and `nothing to commit, working tree clean` before continuing.

5. Pull the latest version of `main`:

   ```bash
   git pull origin main
   ```

If Git says `Already up to date.`, you already have the latest changes. Otherwise, a successful pull may show `Updating`, `Fast-forward`, and a summary of changed files. If Git reports an error about divergent branches or merge conflicts, ask someone for help before continuing.

## 2. Create a branch in VS Code

A branch lets you work on a change separately from `main`.

1. After pulling, click **main** in the **bottom-left corner** of VS Code.
2. Select **Create new branch...** in the menu that opens.
3. Enter a short, descriptive name, such as `add-scatterplot`, and press **Enter**. Use hyphens instead of spaces.
4. Confirm that the bottom-left corner now shows your new branch name.

VS Code automatically switches to the branch you created. Make your edits on this branch. Throughout this guide, replace `add-scatterplot` with the branch name you chose. 

## 3. Make commits in VS Code

A commit records a snapshot of your changes on your computer. Saving a file and committing it are separate steps.

1. Edit your files and save them with **Ctrl+S** on Windows/Linux or **Cmd+S** on macOS.
2. Check the bottom-left corner to confirm you are on your working branch.
3. Click the **Source Control** icon in the left sidebar (the branching icon), or select **View > Source Control**.
4. Under **Changes**, click each file to review your edits.
5. Hover over each file you want to include and click the **+** button to stage it. Staging selects changes for the next commit; the files move to **Staged Changes**. (IF YOU PRESS THE CURVED ARROW, IT WILL REVERT YOUR CHANGES. DO NOT DO THIS.)
6. In the message box at the top of Source Control, enter a short description, such as `Add scatterplot of player statistics`.
7. Click **Commit** (the checkmark button).

Repeat these steps as you finish related pieces of work. Commits stay on your computer until you push them. 

## 4. Push your branch from the terminal

Pushing uploads your commits to GitHub so others can see them.

1. Use the terminal at the bottom of your screen.
2. Run `git status` to confirm you are on your working branch and have committed the changes you want to share.
3. For the first push of this branch, run:

   ```bash
   git push -u origin add-scatterplot
   ```

   Replace `add-scatterplot` with your branch name. Sign in to GitHub if prompted.

The `-u` option connects your local branch to its matching branch on GitHub. If you want to push again later while on that same branch, run:

```bash
git push
```

Every time you push, you send any new commits to GitHub. However, if you then, after pushing, make more commits, you will need to push again and reupdate your GitHub branch.

## 5. Open a pull request on GitHub

A pull request (PR) proposes merging your branch into `main` so others can review your work.

1. After pushing, open the [project repository on GitHub](https://github.com/antmui1/F26-NSDC-Data-Visualization).
2. Click **Compare & pull request** in the banner for your recently pushed branch. If the banner is missing, go to **Pull requests > New pull request**.
3. Check the branch selections:
   - **base:** `main` (the destination for your changes).
   - **compare:** `add-scatterplot` (or your branch name, containing your changes).
4. Review the commits and changed files to confirm the PR includes your intended work.
5. Add a descriptive title and a description explaining what changed, why, and how you checked that it works.
6. Click **Create pull request**. Request a reviewer if appropriate.

If you receive feedback, edit your files on the same branch, commit in VS Code, and run `git push` again. The PR updates automatically. Opening the PR starts the review process; merging it is a separate step. 

## 6. Reviewing and merging

Currently, I (Anthony) am the only one that can review PRs. However, later on, I will open this up to everyone. After a PR is approved, go into the PR on GitHub and press Squash and Merge.

Repeat the cycle every time you make a development.