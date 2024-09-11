## 3. Creating a new repository on GitHub and cloning it to your local machine

[Home](README.md)

Often times, you'll be working with code that someone has already worked on and published to GitHub. In this case, you'll want to clone the repository to your local machine so you can make changes to it. Cloning a repository creates a copy of the repository on your local machine, including all the files and the entire history of the project.

### Exercise 3.1

This exercise will guide you through creating a new repository on GitHub and cloning it to your local machine.

1. Go to [https://github.com/new](https://github.com/new) and create a new repository called `my-github-repo`.
2. When creating your repository, be sure to check the box that says "Initialize this repository with a README". This will create a `README.md` file in your repository. Click the green "Create repository" button to create the repository.
3. Click on the green "Code" button on the next page. By default, it will offer you the HTTPS URL. We will use the SSH key option because we authenticated our terminal using SSH. Click on the SSH link to switch to the SSH key. Copy the key of the repository. It should look something like `git@github.com:username/my-github-repo.git`.
4. In your terminal, navigate to a directory where you want to clone the repository.
5. Run `git clone <key>` to clone the repository to your local machine. Replace `<key>` with the SSH key you copied from GitHub.
   - **git clone:** Clones a repository from a remote server to your local machine. The first argument is the URL of the repository you want to clone.
6. Navigate into the `my-github-repo` directory. Notice that there is a `README.md` file in the directory. This is the file that was created when you initialized the repository on GitHub.
7. Try making some changes to the `README.md` file, adding the changes to the staging area, committing the changes, and pushing them to GitHub.

Congratualtions! You've created a new repository on GitHub and cloned it to your local machine.

[Next: Collaborating with Others on GitHub](04_collaborating_with_others.md)
