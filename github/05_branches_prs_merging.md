## 5. Branches, PRs, and Merging

[Home](README.md)

Git is a powerful tool for making updates to your code efficiently. It allows you to work on different features or bug fixes in parallel, and then merge them together when they are ready. This section will cover the basics of branches, pull requests, and merging in Git.

Some definitions:

- **Branch**: A branch is a parallel version of a repository. It is used to work on a feature or bug fix without affecting the main codebase. When you create a branch, you are creating a copy of the code at that point in time, and you can make changes to it without affecting the main codebase.
- **Pull Request (PR)**: A pull request is a request to merge changes from one branch into another. It allows you to review the changes made in the branch and discuss them with other contributors before merging them into the main codebase.
- **Merging**: Merging is the process of combining the changes from one branch into another. When you merge a branch into another, the changes made in the branch are applied to the target branch.

### Exercise 5.1

In this exercise, you will learn how to create a new branch in your repository and switch between branches.

0. Before we start, it's good practice to make sure your code is up to date. Run the following commands to pull the latest changes from the `main` branch:
   ```
   git checkout main
   git pull origin main
   ```
   - **git checkout:** Switches to the specified branch. In this case, `main`.
1. Create a new branch in your `my-github-repo`, then switch to it:

   ```bash
    # Create a new branch:
   git branch new-branch

   # Switch to the new branch:
   git checkout new-branch
   ```

   You can also combine these two commands into one by doing `git checkout -b new-branch`.

2. Make some changes to the `README.md` file in your new branch. For example, add a new section to the file. Note that any changes you make while on the new branch will not affect the `main` branch.
3. Add the changes to the staging area, commit the changes, and push the changes to GitHub.

Congratulations! You've created a branch in your repository and made changes to it.

### Exercise 5.2

Next, you will learn how to create a pull request to merge your changes from the new branch into the `main` branch.

1. Go to your repository on GitHub. You can see your newly created branch by clicking on the dropdown with the branch icon on the left (which should currently say main) and selecting your new branch.
2. Navigate to the "Pull requests" tab and click on the "New pull request" button.
3. Select the `main` branch as the base branch and your new branch as the compare branch.
4. Review the changes you made in your new branch and create the pull request.
5. Add a title and description for your pull request, and then click on the "Create pull request" button.

Congratulations! You've created a pull request to merge your changes from the new branch into the `main` branch. Pull requests are allow you to review the changes made in the branch and discuss them with other contributors before merging them into the main codebase. The role of a _PR manager_ is to review and merge pull requests. In a professional setting, the PR manager is typically a senior developer or team lead. Here, you are your own PR manager.

### Exercise 5.3

Finally, you will learn how to merge your changes from the new branch into the `main` branch.

1. Go to your repository on GitHub and navigate to the "Pull requests" tab.
2. Click on the pull request you created in the previous exercise.
3. Review the changes and make sure everything looks good.
4. Click on the "Merge pull request" button to merge your changes into the `main` branch.
5. Confirm the merge. At this point, you have the option to delete the branch after merging. This is a good practice to keep your repository clean, but sometimes you may want to keep the branch for future reference or to continue working on it.
6. Check out the main branch on your repository on GitHub and notice that the changes from your new branch have been merged into the `main` branch.
7. Don't forget to update your local repository. On your machine, run the following commands to switch back to the `main` branch and pull the latest changes:
   ```
   git checkout main
   git pull origin main
   ```

Congratulations! You've merged your changes from the new branch into the `main` branch. Merging is the process of combining the changes from one branch into another. When you merge a branch into another, the changes made in the branch are applied to the target branch.

[Next: A Software Engineering Workflow Using Github](06_software_engineering_workflow.md)
