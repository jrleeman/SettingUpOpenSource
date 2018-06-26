# CI with TravisCI

## Objectives

- Learn what Continuous Integration is
- Set up Travis CI on a GitHub repository
- Configure Travis CI for multiple test builds

**Duration: 45 minutes**

### What is Continuous Integration?

- Changes are continually integrated into main branch of software
- This is enabled by running suite of tests for every change made to the code base
- Variety of GitHub-integrated services
  - Travis-CI: Linux, OSX
  - Appveyor: Windows, Linux (new)
  - CircleCI: Linux, OSX (docker containers)
- These services can run on every Pull Request--make sure the PR doesn't break anything
- Pull Requests can be configured to require checks to pass before merge
- We'll be setting up Travis-CI

### First steps: Initial Travis config for a single Python version (3.6)

- Sign into https://travis-ci.com with GitHub
- Configure Travis to run for our repository
- Make a local branch
- Create `.travis.yml`
```yml
language: python
sudo: false

# Only run on master since we'll be using branches for our PR
branches:
  only:
    - master

# What Python version to use
python:
  - 3.6

# How do we install?
install:
  - pip install .

# How do we test?
script:
  - pytest
```
- Individual sections (`install`, `script`) become shell scripts
- Commit and push to remote repository; make Pull Request
- See what the PR looks like, the status checks
- Break Time

### More modifications
- Run on Python 2.7, 3.5, 3.6
- Install dependencies (`before_install`)
- Use environment variable to install miniconda
```yml
matrix:
  include:
    - python: 3.6
      env: MINICONDA="y"

before_install:
  - |
    if [[ $MINICONDA == "y" ]]; then
      wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
      bash miniconda.sh -b -p $MINICONDA_DIR
      export PATH="$MINICONDA_DIR/bin:$PATH"
      hash -r
      conda config --set always_yes yes --set changeps1 no
      conda update -q conda
      conda info -a
      conda install numpy
    fi
```

### More things possible
- https://docs.travis-ci.com
- Deploy build products to S3
- Push to docs to GitHub Pages
- Deploy built packages to PyPI
- Push code coverage results to another service
- Send notification to another webhook