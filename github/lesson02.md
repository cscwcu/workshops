## 2. Creating a local repository and pushing it to GitHub

Now that you know how to create a new repository and make changes to it, let's push it to GitHub. GitHub is a web-based platform that allows you to store and manage your code in the cloud. It also provides tools for collaborating with others on your projects.

If you don't already have a GitHub account, you can create one at [https://github.com/signup](https://github.com/signup).

### Exercise 2.1

1. Go to [https://github.com/new](https://github.com/new) and create a new repository called `my-repo`.
2. Copy the URL of the repository. It should look something like `https://github.com/your-username/my-repo`.
3. In your terminal, run `git remote add origin <url>` to add the remote repository to your local repository. Replace `<url>` with the URL of your repository.

- **git remote add:** Adds a new remote repository to your local repository. A remote repository is a version of your repository that is hosted on a server, such as GitHub. The first argument is the name of the remote (in this case, `origin`), and the second argument is the URL of the remote repository.

4. Run `git push -u origin master` to push your local repository to GitHub.

- **git push:** Pushes your local repository to a remote repository. The `-u` flag sets the upstream branch for the current branch, so that in the future, you can use `git push` without any arguments to push your changes to the remote repository.

Now if you go to your repository on GitHub (you may need to refresh the page), you should see the `hello.txt` file you created in your local repository.

### Exercise 2.2

Now that your repository is on GitHub, you can make changes to it from your local machine and push them to GitHub. This exercise will guide you through making some changes to your repository and pushing them to GitHub.

1. Open the `hello.txt` file in your text editor and make some changes to it.
2. Run `git status` to see the current state of your repository. You should see that `hello.txt` has been modified.
3. Run `git add hello.txt` to add the changes to the staging area.
4. Run `git commit -m "Update hello.txt"` to commit the changes to the repository.
5. Run `git push` to push the changes to GitHub.

Now if you go to your repository on GitHub, you should see the changes you made to `hello.txt`.
