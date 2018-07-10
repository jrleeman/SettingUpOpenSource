# Read the Docs

## Objectives
* Understand services provided by Read the Docs
* Setup project documentation
* Build docs on TravisCI

**Duration: 30 minutes**

## Setting up ReadTheDocs

**Activity**
Go to [readthedocs.org](https://readthedocs.org/) and sign up for a
free account. Login to the new account.

---

Next, we need to connect our read the docs account to GitHub so it can see
our repositories and setup webhooks for us.

* Click the down arrow by your user name in the upper right of the page.
* Select settings
* Select "Connected services" from the left hand navigation menu.
* Click the "Connect to GitHub" button and authorize the application.

---

Now we need to connect our project repository to read the docs and get the
doc build going.

* Click on your user name to get to the dashboard.
* Click the "Import a project" button.
* Click the plus button by the project you'd like to import.

---
**Tip**
If you don't choose to link your GitHub account, there is a manual import
feature. You provide the link to your repository and then manually setup the
web hook following the documentation.

## Building docs on Travis
* Add `- make html` to the script step.
* Time permitting discuss adding a build matrix item using environment variables.
