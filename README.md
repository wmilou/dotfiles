# 📌 Dotfiles by Wedsley – Stow-Powered Configs 

## 🚀 Introduction
GNU Stow is a powerful symlink manager that simplifies the management of dotfiles across multiple environments. By leveraging Stow, you can keep your dotfiles organized in a Git repository and easily deploy them on any system with minimal effort.

---

## 🛠️ Installation
Before using Stow, ensure it is installed on your system.

### 🐧 Linux (Debian/Ubuntu)
```sh
sudo apt update && sudo apt install stow
```

### 🍏 macOS (via Homebrew)
```sh
brew install stow
```

### 🏁 Arch Linux
```sh
sudo pacman -S stow
```

---

## 📂 Organizing Your Dotfiles

A common approach is to store your dotfiles in a Git repository using the following structure:

```
~/.dotfiles/
  ├── git/
  │   ├── .gitconfig
  │   ├── .gitignore
  ├── nvim/
  │   ├── .config/nvim/init.vim
  ├── zsh/
  │   ├── .zshrc
  ├── tmux/
  │   ├── .tmux.conf
```
Each folder represents a package containing related configuration files.

---

## 🔗 Using Stow to Manage Dotfiles

### 1️⃣ Cloning Your Dotfiles Repository
First, clone your dotfiles repository to your home directory:
```sh
git clone https://github.com/wmilou/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
```

### 2️⃣ Deploying Dotfiles with Stow
To create symlinks for a specific package (e.g., `zsh`):
```sh
stow -v zsh
```
This will link `.zshrc` from `~/.dotfiles/zsh/.zshrc` to `~/.zshrc`.

To deploy multiple configurations at once:
```sh
stow -v git nvim tmux
```

### 3️⃣ Removing Symlinks
If you need to remove a package’s symlinks (without deleting the actual files), use:
```sh
stow -D zsh
```

### 4️⃣ Handling Conflicts
If a file already exists in your home directory, Stow will throw an error. You can back up the existing file and retry:
```sh
mv ~/.zshrc ~/.zshrc.backup
stow -v zsh
```

---

## 🎯 Best Practices
- Always track your dotfiles repository with Git:
  ```sh
  git add .
  git commit -m "Update dotfiles"
  git push origin main
  ```
- Use separate folders for different applications to keep configurations modular.
- Regularly sync your dotfiles across devices by pulling the latest changes:
  ```sh
  git pull origin main && stow -v */
  ```

---

## 🎉 Conclusion
Using GNU Stow is a clean and efficient way to manage dotfiles. By structuring your dotfiles repository correctly, you can easily deploy, update, and maintain configurations across multiple environments effortlessly.

Now, setting up a new system is as simple as cloning your repo and running `stow`! 🚀🔥

