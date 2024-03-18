## 6. A software engineering workflow using GitHub

[Home](README.md)

In this section, we will simulate a typical software engineering workflow using GitHub. This workflow will include creating a new branch, making changes to the branch, creating a pull request, and merging the changes into the main branch.

To get started, be sure you've forked and cloned the `github-workshop` repository to your local machine. You can find it at [https://github.com/wcucs/github-workshop](https://github.com/wcucs/github-workshop). You will have to fork the repository first because you won't have permission to push changes to the original repository. Once you've done this, you can clone your fork to your local machine.

To fork the repository, follow these steps:

1. Go to the repository's page on GitHub. Click on the "Fork" button in the top-right corner of the page. This will create a copy of the repository under your GitHub account.
2. After forking, you will be redirected to your forked repository.
3. Clone this repository to your local machine using the `git clone` command and the URL from your forked repository.

Now we can get started with the workflow. Your task is to fix a bug in the `heapify.py` file and create a pull request to merge your changes into the `main` branch.

**Hint**: There are three bugs in the `heapify.py` file. See if you can find and fix them all. Additionally, good practice is to commit your changes after fixing each bug.

1. **Create a new branch**: Before we start making changes to the code, we'll create a new branch to work on. This is a good practice because it allows us to work on new features or bug fixes without affecting the `main` branch. Create a new branch with your username as the name of the branch.
2. **Make some changes**: Now that you're on your new branch, open the file `heapify.py`. This code is buggy. See if you can identify the problem and fix it.
3. **Add, commit, and push**: Once you've made your changes, add them to the staging area, commit them, and push them to GitHub. Be sure to make your commit message meaningful; it should describe the changes you made or the problem you fixed.
4. **Create a pull request**: Go to your repository on GitHub and create a pull request to merge your changes from your new branch into the `main` branch. Be sure that you are attempting to merge from your forked repository into the original repository. You can do this by selecting the original repository (`wcucsc/github-workshop`) as the base repository and the `main` branch as the base branch. Be sure to also include a title and description for your pull request.
5. **Review and merge**: At this stage, a PR manager will review the changes. If the changes are approved, you will be able to merge your changes into the main branch. Once the changes are merged, you can delete your branch if you'd like.

Congratulations! You've completed a software engineering workflow using GitHub. This is a simplified version of what you might encounter in a professional setting, but it covers the basics of working with branches, pull requests, and merging changes. These are fundamental concepts that you will use in your day-to-day work as a student and as a software engineer.

[Next: End](end.md)
