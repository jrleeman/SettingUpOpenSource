# Testing

## Objectives
* Setup our sample project for testing
* Discuss types of tests
* Write tests using PyTest
* Run the test suite
* Practice test driven development
* Check the test coverage of our project

**Duration: 60 minutes**

Testing is the only way to keep your code base maintained on multiple versions
of Python, ensure its accuracy against known cases, and prevent regressions. In
this lesson, we'll go over the basics to testing, setup a test suit on our
project, run it locally, and then run it on TravisCI. Finally, we'll check the
test coverage on our project.

### Add (canned) library code to repository
For us to write tests, we'll need come code to test. To save time, we've 
provided code for a simple library in the tutorial's repository.

* Download the zip of the github repository (or clone if you prefer)
* Copy the library folder `hugs` into the base of your repository.
* Commit and push this with `git add -A`, then `git commit -m "Adding library code"`

The `hugs` library (**h**ugely **u**seful **g**eoscience **s**tuff)
is a demo library that we've created for this tutorial. It contains
some geology/geophysics and atmospheric science equations and plots
that we can write tests for.

### Writing tests with PyTest
PyTest is one of the most commonly used Python testing frameworks. We are 
going to cover the basic concept of test writing and explore the test
coverage of the `hugs` library.

There are many types of software testing and schools of thought on it,
but here we'll define a few terms and how we'll be using them in the
context of this tutorial.

**Unit Testing** - Testing a single unit of code (function, method, etc)
for the correct or expected outputs.

**Integration Testing** - Testing that multiple segments of code can
function together as expected.

**Regression Testing** - Testing that previously developed functionality
or bug fixes still function as expected.

Another buzz-word is test-driven-development (TDD). This is the process
of writing the test for the expected behavior and API before development
of the code. For example, writing the test for the correct output of a
function before fixing a reported bug.

---

* First we need to install `PyTest`. Do this with `conda install PyTest
* Verify your installation with `pytest --version`

--- 

Pytest looks for files named `test*.py` and will run the functions named
`test*` in those files. Let's create our first test.

### Running tests
* Now that we're created a test, it's time to run it. Run the test with
  `pytest` and observe the results.
* Change something to break the test and see the results.

**Activity** Write tests for the functions `x` and `x` and make them
pass.

### Other Common Tests
#### Test that an exception is raised
* Use the raises helper to write a test for `x` and ensure that a
`ValueError` is raised.

#### Temporary Directories
* When a test needs a temporary directory to write a file to, there
  are easy ways to do this.

### Coverage with coverage.py and pytest-cov
