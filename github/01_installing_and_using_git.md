## 1. Installing and using git on the command line

[Home](README.md)

To install git on your local machine, go to [https://git-scm.com/downloads](https://git-scm.com/downloads) and download the appropriate version for your operating system.

Git is installed on Agora, so if you can't install it now, you can use it there for the next steps.

The main git work flow involves making changes to a file, adding those changes to the staging area, and then committing those changes to the repository. Before we continue, let's define a repository:

- **Repository (repo):** A repository is a collection of files and folders that are tracked by Git, such as your code files. It contains the entire history of the project, including all the commits and branches.

Here's an example of how I can make a change to a file in my project and commit it:

```bash
# Make a change to a file
echo "Hello, world!" > hello.txt

# Add the change to the staging area
git add hello.txt

# Commit the change to the repository
git commit -m "Add hello.txt"
```

Some quick definitions:

- **Staging area:** The staging area is a place where you can group changes together before committing them to the repository. This allows you to commit only the changes you want, rather than all the changes in your working directory.
- **Commit:** A commit is a snapshot of the changes you've made to your code. It's like taking a picture of your project at a specific point in time. Each commit has a unique ID, a message describing the changes, and a pointer to the previous commit.

Now the file `hello.txt` is tracked by git and the change is saved in the repository. If I make more changes to the file...

```bash
# Make another change to the file
echo "Goodbye, world!" > hello.txt

# Add the change to the staging area
git add hello.txt

# Commit the change to the repository
git commit -m "Update hello.txt"
```

Git saves the history of the file, so I can always go back to the previous version if I need to. This is good because it allows me to experiment with my code without worrying about breaking it and not being able to go back to when it worked.

### Exercise 1.1

The commands you will use the most in your git workflow are `git status`, `git add`, `git commit`, and later `git push`. `git status` shows you the current state of your repository, `git add` adds changes to the staging area, and `git commit` saves the changes to the repository. This exercise will guide you through creating a new repository and making some changes to it.

1. Open a terminal and navigate to a directory where you want to create a new repository. You may use your root directory.
2. Create a new directory called `my-repo` and navigate into it.
3. Run `git init` to create a new git repository in the current directory.

- **git init:** Initializes a new git repository in the current directory. This creates a hidden directory called `.git` that contains all the information git needs to track changes to your files.

4. Run `git status` to see the current state of the repository. You should see that there are no files being tracked by git.
5. Create a new file called `hello.txt` and add some text to it.
6. Run `git status` again. You should see that `hello.txt` is an untracked file.
7. Run `git add hello.txt` to add the file to the staging area.
8. Run `git status` again. You should see that `hello.txt` is now a new file in the staging area.
9. Run `git commit -m "Add hello.txt"` to commit the changes to the repository.
10. Run `git status` one more time. You should see that there are no changes to commit.

Congratulations! You've created a new repository and made some changes to it. You can use `git log` to see the history of your repository, and `git diff` to see the changes you've made to your files.

[Next: Creating a local repository and pushing it to GitHub](02_creating_a_local_and_pushing.md)
