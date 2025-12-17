# Git Instructions for "Week 9: Git and GitHub"

**IMPORTANT: Follow these commands EXACTLY. The commit messages must be PRECISE.**

## Prerequisites
1.  Open your terminal (Git Bash).
2.  Navigate to the repository folder:
    ```bash
    cd ~/Desktop/Repository/MyFirstRepo
    ```

## Task 0: Create and Manage Your First Repository

1.  **Initialize and Add Files:**
    ```bash
    git init
    git add README.md introduction.txt
    ```
2.  **Commit (Exact Message Required):**
    ```bash
    git commit -m "Added introduction file"
    ```
3.  **Push to GitHub:**
    *Replace `your-username` with your actual GitHub username.*
    ```bash
    git remote add origin https://github.com/your-username/MyFirstRepo.git
    git branch -M main
    git push -u origin main
    ```

## Task 1: Working With Branches and Making Pull Requests

1.  **Create Branch:**
    ```bash
    git checkout -b feature-update
    ```
2.  **Add File:**
    ```bash
    git add goals.txt
    ```
3.  **Commit (Exact Message Required):**
    ```bash
    git commit -m "Added goals list"
    ```
4.  **Push Branch:**
    ```bash
    git push origin feature-update
    ```
5.  **Action on GitHub:**
    - Go to your repository on GitHub.
    - You should see a "Compare & pull request" button. Click it.
    - Create the Pull Request.
    - Merge the Pull Request into `main`.

## Task 2: Collaborating via Forking (Do this on GitHub Website)

1.  Go to the [sample repository](https://github.com/alex-learning/learn_github_collaboration) (or the link provided in your project).
2.  Click **Fork** (top right) to copy it to your account.
3.  In *your* forked repository, edit `README.md`.
4.  Add your name to the list.
5.  **Commit changes** with message: `"Added my name to contributors list"`.
6.  Go to the **Pull Requests** tab and create a New Pull Request.
7.  Set the title/description to: `"Added my name to the list of contributors"`.
8.  Submit.

## Task 3: Cloning, Editing Locally, and Syncing

1.  **Switch to Main and Update:**
    ```bash
    git checkout main
    git pull origin main
    ```
2.  **Add File:**
    ```bash
    git add learning.txt
    ```
3.  **Commit (Exact Message Required):**
    ```bash
    git commit -m "Added learning.txt with course reflection"
    ```
4.  **Push:**
    ```bash
    git push origin main
    ```

### Troubleshooting Task 3
If you get an error about the commit message for Task 3, run this command to fix the message of your last commit:
```bash
git commit --amend -m "Added learning.txt with course reflection"
git push -f origin main
```
