# GitHub Workshop

#### Author(s): CS Club @ WCU

Last revised: 02-23-2024

## Description

This workshop will cover the basics of using GitHub. We will cover the following topics:

- Installing and using git on the command line
- Creating a local repository and pushing it to GitHub
- Creating a new repository on GitHub and cloning it to your local machine
- Collaborating with others on GitHub
- Branches, PRs, and merging
- A software engineering workflow using GitHub

## 0. Preface: What is Git?

**Introduction to VCS and Git**

A version control system (VCS) is a tool that helps you manage changes to your code over time. It allows you to revert to previous versions, track changes, and collaborate with other developers.

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It enables multiple developers to work together on the same project without interfering with each other's work. This workshop will introduce you to the basics of Git, GitHub, and how to use them to manage your code. We will also cover GitHub and some best practices for collaborating with others on a project.

## 1. Installing and using git on the command line

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

## 3. Creating a new repository on GitHub and cloning it to your local machine

Often times, you'll be working with code that someone has already worked on and published to GitHub. In this case, you'll want to clone the repository to your local machine so you can make changes to it. Cloning a repository creates a copy of the repository on your local machine, including all the files and the entire history of the project.

### Exercise 3.1

This exercise will guide you through creating a new repository on GitHub and cloning it to your local machine.

1. Go to [https://github.com/new](https://github.com/new) and create a new repository called `my-github-repo`.
2. When creating your repository, be sure to check the box that says "Initialize this repository with a README". This will create a `README.md` file in your repository.
3. Copy the URL of the repository.
4. In your terminal, navigate to a directory where you want to clone the repository.
5. Run `git clone <url>` to clone the repository to your local machine. Replace `<url>` with the URL of your repository.
6. Navigate into the `my-github-repo` directory. Notice that there is a `README.md` file in the directory. This is the file that was created when you initialized the repository on GitHub.
7. Try making some changes to the `README.md` file, adding the changes to the staging area, committing the changes, and pushing them to GitHub.

Congratualtions! You've created a new repository on GitHub and cloned it to your local machine.

## 4. Collaborating with others on GitHub

One of the most powerful features of GitHub is its ability to facilitate collaboration between developers. GitHub provides tools for managing issues, reviewing code, and merging changes from multiple contributors. This section will cover some of the basics of collaborating with others on GitHub.

### Exercise 4.1

First, let's suppose you're working on a project, and your project partner lets you know that they've made some changes to the code. You'll want to pull those changes to your local machine so you can work with the most up-to-date version of the code.

1. Clone the following repository to your local machine: [https://github.com/wcucs/github-workshop](https://github.com/wcucs/github-workshop).
2. Navigate into the `github-workshop` directory. What does the `README.md` file say?
3. Now, I'll make a change to the file from my machine.
4. Run `git pull` to pull the changes from the remote repository to your local repository. What does the `README.md` file say now?

Congratulations! You've pulled changes from a remote repository to your local repository. This is what the majority of your GitHub workflow will look like when working with other people: making changes to the code, pushing them to GitHub, and pulling changes from GitHub to your local machine.
