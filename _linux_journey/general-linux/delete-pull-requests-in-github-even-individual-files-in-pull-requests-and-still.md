---
title: "Delete pull requests in GitHub and Still Keep the PR Up"
category: "general-linux"
tags: ["delete", "pull", "requests", "github", "even"]
---

# Delete pull requests in GitHub and Still Keep the PR Up

This even works for PRs that are to be merged from a fork.

For example, I fork the Rocky Linux Docs repository. I then edit the files in my fork and then submit a PR from my fork back to the Rocky Linux Docs repository. If I want to remove individual files from the PR, but still keep the PR up, I can do that via the below commands.

The files are not only removed from my fork of the repository, but also from the PR that is sent to Rocky Linux Docs.

https://graphite.com/guides/delete-pull-requests-in-github

This guide explores how to close pull requests, delete branches related to closed pull requests, and delete specific files within pull requests. We'll also discuss the differences between closing and deleting PRs, and how to reopen them if necessary.

Understanding the terms: closing vs. deleting pull requests
Closing a pull request:

Closing a pull request in GitHub signifies that the PR is complete, rejected, or no longer relevant, but it does not delete the PR from GitHub. It remains in the repository's history and can be reopened or referenced in the future.
To close a pull request, you simply change its status to "closed" on the GitHub interface, indicating that the PR should not be merged into the base branch.
Deleting a pull request:

GitHub does not provide a direct way to delete a pull request because it serves as a part of the project's historical documentation. However, you can delete the branch associated with a closed pull request, which effectively removes the proposed changes from being merged.
Deleting the branch of a closed pull request is common to tidy up your repository once the changes are merged or definitively rejected.
Step-by-step guide to manage pull requests
Close a pull request on GitHub
Navigate to the pull request: Go to the "Pull Requests" section of your repository.
Choose the pull request to close: Select the pull request you wish to close.
Close the pull request: At the bottom of the pull request page, click the "Close pull request" button to close it without merging the changes.
Reopen a closed pull request
If a closed pull request needs to be reconsidered, you can easily reopen it:

Navigate to the closed pull request: Go to the "Closed" tab under "Pull Requests".
Select the pull request: Find the pull request you wish to reopen.
Reopen the pull request: Click the "Reopen pull request" button to move it back to an open state.
Delete a branch after closing a pull request
Once a pull request is merged or closed, you might want to delete the branch to clean up your repository:

Navigate to the pull request: Access the closed or merged pull request.
Delete the branch: If the pull request was merged, you can delete the branch directly from the pull request page. If you closed the pull request or it was merged successfully, you can delete the branch by clicking the "Delete branch" button.
Delete a file from an open pull request
If you need to remove a file from an existing pull request:

Check out the branch associated with the pull request: Use Git to switch to the branch:
Terminal
git checkout feature-branch


Delete the file: Remove the file using the git command:
Terminal
git rm file-to-delete.txt
git rm --cached is also a good way to do it, then you don't remove the files in your local directory, the files are only removed from the online PR itself.


Commit the change: Commit your changes with a message explaining the deletion:
Terminal
git commit -m "Remove unnecessary file"


Push the changes: Update the branch on GitHub, which will automatically update the pull request:
Terminal
git push origin feature-branch


Deleting an open pull request
To remove an open pull request without merging:

Close the pull request: Follow the steps above to close the pull request without merging it.
Delete the branch: As described above, you can delete the branch to effectively remove the changes proposed in the pull request.
For more information, see the official GitHub documentation.
