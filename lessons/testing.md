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
  `https://github.com/jrleeman/SettingUpOpenSource
* Copy the library folder `hugs` and `setup.py` into the base of your
  repository.
* Commit and push this with `git add -A`, then `git commit -m "Adding library
  code"`

The `hugs` library (**h**ugely **u**seful **g**eoscience **s**tuff)
is a demo library that we've created for this tutorial. It contains
some geology/geophysics and atmospheric science equations and plots
that we can write tests for.

### Activate and install hugs
* Activate the environment we created for the workshop `conda activate suos`
  If you didn't setup the environment before we started, run `conda env create`
  in the root of the repository.
* In the base directory of the repository, install an editable version of the
  hugs library (uses `setup.py`) with `pip install -e .`

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
`test*` in those files.

* Run the current test suite with `pytest` and observe the results.
* Change a test result so that the tests will break and run again to see
  what a test failure looks like.

### Creating Tests

**Activity**
* Write a test for the function `get_wind_components` to verify that it works
  with scalar values for the speed and direction.
* Write another test for `get_wind_components` to verify that it works on
  an array of values. Write the array to test every 45 degrees of the compass
  including the end-member cases of 0 degrees and 360 degrees.

**Solution**
```python
  def test_wind_comps_basic():
      """Test the basic wind component calculation."""
      speed = np.array([4, 4, 4, 4, 25, 25, 25, 25, 10.])
      dirs = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360])
      s2 = np.sqrt(2.)

      u, v = get_wind_components(speed, dirs)

      true_u = np.array([0, -4 / s2, -4, -4 / s2, 0, 25 / s2, 25, 25 / s2, 0])
      true_v = np.array([-4, -4 / s2, 0, 4 / s2, 25, 25 / s2, 0, -25 / s2, -10])

      assert_array_almost_equal(true_u, u, 4)
      assert_array_almost_equal(true_v, v, 4)


  def test_wind_comps_scalar():
      """Test wind components calculation with scalars."""
      u, v = get_wind_components(8, 150)
      assert_almost_equal(u, -4, 3)
      assert_almost_equal(v, 6.9282, 3)
```

### Other Common Tests

#### Test that a warning is raised
Some functions will raise warnings and we want to ensure that indeed that is
happening. We can use `pytest.warns` to check this. It's used as a context
manager.

**Activity**
* Add a test to verify that the `get_wind_components` function to verfiy that
  a warning is raised when the wind direction is greater than 360 degrees. Don't
  forget to verify that your test is working by first by using values that will
  not raise a warning.

**Solution**
```python
def test_warning_direction():
    """Test that warning is raised wind direction > 360."""
    with pytest.warns(UserWarning):
        get_wind_components(3, 480)
```

#### Test that an exception is raised
In cases where an exception is raised, we want to check that it indeed is as
well. We do this similarly to the warning check using `pytest.raises` as a
context manager.

```python
def test_snell_zero_velocity_top():
    """That that a value error is raised with a zero velocity top layer."""
    with pytest.raises(ValueError):
        snell_angle(12, 0, 4000)
```

### Coverage with coverage.py and pytest-cov
We also want to know what the test coverage of our library is - have we missed
anything? We can use coverage.py to check this and pytest-cov lets us do run this
tool on all of our test suite and see the total library coverage.

* Run `py.test --cov=hugs`
* Add a function with no tests
* Run it again
* Remove the added function
