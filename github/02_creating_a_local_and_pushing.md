## 2. Creating a local repository and pushing it to GitHub

[Home](README.md)

Now that you know how to create a new repository and make changes to it, let's push it to GitHub. GitHub is a web-based platform that allows you to store and manage your code in the cloud. It also provides tools for collaborating with others on your projects.

If you don't already have a GitHub account, you can create one at [https://github.com/signup](https://github.com/signup).

### Before we continue

To interact with your GitHub repositories from your terminal, you need to authenticate your machine with GitHub. One of the most secure and convenient methods for doing this is by using SSH keys.

#### Step 1: Generating an SSH Key

1. Open your terminal and run the following command to generate a new SSH key:

   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

   - `-t rsa` specifies that you want to use the RSA algorithm (which is the most commonly used algorithm for SSH keys).
   - `-b 4096` specifies the length of the key, with 4096 bits providing a high level of security.
   - `-C` allows you to add a comment, usually your email address, to identify the key.

2. When prompted to "Enter a file in which to save the key," press Enter to accept the default location.

   ```bash
   Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
   ```

3. You'll then be asked to enter a passphrase. You can press Enter to leave this blank (not recommended for security purposes), or enter a secure passphrase.

#### Step 2: Adding Your SSH Key to the SSH Agent

Before adding the key to GitHub, you need to ensure that the SSH agent is running and add your SSH key to the agent.

1. Start the SSH agent in the background:

   ```bash
   eval "$(ssh-agent -s)"
   ```

2. Add your SSH private key to the SSH agent:

   ```bash
   ssh-add ~/.ssh/id_rsa
   ```

#### Step 3: Adding the SSH Key to Your GitHub Account

1. Copy the SSH key to your clipboard by running:

   ```bash
   pbcopy < ~/.ssh/id_rsa.pub
   ```

   If `pbcopy` isn’t available (on Windows or Linux), you can manually open the key file and copy it.

   ```bash
   cat ~/.ssh/id_rsa.pub
   ```

2. Go to your GitHub account:
   - In the upper-right corner, click on your profile photo, then click **Settings**.
   - In the left sidebar, click **SSH and GPG keys**.
   - Click **New SSH key**.
   - In the "Title" field, add a descriptive label for the new key, for example, "My Laptop Key."
   - Paste your SSH key into the "Key" field.
   - Click **Add SSH key**.

#### Step 4: Testing Your Connection

To make sure your SSH key is working correctly, run the following command:

```bash
ssh -T git@github.com
```

You should see a message like:

```bash
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

This means your SSH key is set up correctly, and you're authenticated with GitHub.

---

Now that you've set up SSH, you can continue with pushing your repository to GitHub. Use the `git remote add` and `git push` commands to securely communicate with GitHub using your SSH connection.

### Exercise 2.1

1. Go to [https://github.com/new](https://github.com/new) and create a new repository called `my-repo`.
2. Copy the URL of the repository. It should look something like `https://github.com/your-username/my-repo`.
3. In your terminal, run `git remote add origin <url>` to add the remote repository to your local repository. Replace `<url>` with the URL of your repository.

   - **git remote add:** Adds a new remote repository to your local repository. A remote repository is a version of your repository that is hosted on a server, such as GitHub. The first argument is the name of the remote (in this case, `origin`), and the second argument is the URL of the remote repository.

4. Run `git push -u origin main` to push your local repository to GitHub.

   - **git push:** Pushes your local repository to a remote repository. Initially, you have to specify the repository (`origin`) and the branch (`main`). The `-u` flag saves these arguments so that in the future you can use `git push` without any arguments to push your changes to the specified branch.

Now if you go to your repository on GitHub (you may need to refresh the page), you should see the `hello.txt` file you created in your local repository.

### Exercise 2.2

Now that your repository is on GitHub, you can make changes to it from your local machine and push them to GitHub. This exercise will guide you through making some changes to your repository and pushing them to GitHub.

1. Open the `hello.txt` file in your text editor and make some changes to it.
2. Run `git status` to see the current state of your repository. You should see that `hello.txt` has been modified.
3. Run `git add hello.txt` to add the changes to the staging area.
4. Run `git commit -m "Update hello.txt"` to commit the changes to the repository.
5. Run `git push` to push the changes to GitHub.

Now if you go to your repository on GitHub, you should see the changes you made to `hello.txt`.

[Next: Creating a New Repository on GitHub and Cloning it to Your Local Machine](03_new_github_repository.md)
