# MyGit - The "Totally Not Git" Version Control System

Welcome to **MyGit**—a version control system for people who love Git but also love pain. Why use something battle-tested when you can reinvent the wheel, right? 🚀

## 🤔 Why MyGit?
Because real Git is too mainstream. Just kidding. This is just a tiny cute project to learn how Git works under the hood (It is too complicated than I thought. obviously!).

---

## 🚀 Getting Started
Before you dive in, make sure you have Python installed. Then add the path of the root directory to paths in environmental variables. 
Now you can initialize a MyGit repository by running:

```sh
mygit init
```
This will create a `.mygit/` directory, which is totally not git.

---

## 🛠 Available Commands
Here’s what you can do with **MyGit** so far, aside from breaking things:

### 1️⃣ `mygit init`  
Initializes a new MyGit repository. Creates a `.mygit/` directory where all the magic (and potential disasters) happen.

### 2️⃣ `mygit add <file>`  
Stages a file for commit. If you don't want to specify a file, just use `mygit add .` it will try to add everything in sight. Yes, even your embarrassing TODO notes.

### 3️⃣ `mygit commit "message"`  
Commits your changes with a message. If you forget `message`, don’t worry. It’ll just commit with `"Fixed some bugs (probably created more)"` as default. Git doesn't have it Right? 😉

### 4️⃣ `mygit status`  
Shows what's changed, what’s staged, and what you’ve forgotten to track. Basically, it tells you how much of a mess you've made.

### 5️⃣ `mygit log`  
Displays the history of commits. Great for pretending you know what’s happening.

### 6️⃣ `mygit when [file]`  
Find out when a file was last modified (or when the entire project was abandoned). Useful for realizing you haven't touched a project in years.

### 7️⃣ `mygit checkout <commit_hash>`  
Reverts your working directory to a specific commit. Good luck with finding the lengthy commit hash.

### 8️⃣ `mygit branch <name>` (Not implemented, but we like to dream)  
Pretend you can create branches. Currently does nothing except boost your self-esteem.

---

## 🎉 Why Use MyGit?
- Because debugging your own version control system is **way more fun** than using Git.
- You’ll appreciate how amazing real Git is after using this.
- And you can learn git with me. One day we'll be the worst enemy of Git.

---

## 👏 Contributing
Want to help improve **MyGit**? Great! Just fork the repo, make changes, and then realize that **MyGit doesn’t have push and pull support yet**.

---

Thank you for using **MyGit**. Or at least reading this far.
