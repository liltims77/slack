git stash is a super handy command when you're working on something, 
but need to quickly switch to another branch or task without committing your changes. 
It temporarily saves your uncommitted changes (both tracked and untracked files 
if specified) and gives you a clean working directory.

1. Save current changes
git stash

2. Save with a message (recommended)
git stash save "my work in progress"
git stash push -m "my work in progress"

3. Include untracked files too
git stash push -u -m "work with untracked"
-u is short for --include-untracked.


✅ Use git fetch if you want to inspect changes first before updating your code.
✅ Use git pull when you trust the remote changes and want to get them right away.

🔹 git fetch gets the updates.
🔹 git pull gets the updates AND applies them to your current branch.


