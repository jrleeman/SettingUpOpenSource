# Flake8

## Objectives
* Discuss why flake tools are necessary and beneficial to a project
* Setup pytest-flake8
* Suppress selected warnings
* Run flake checks as part of a Travis build
* Learn about additional plugins that can enhance your flake setup

**Duration: 20 minutes**

Code style checkers are a great way to ensure that your project has a clean
and consistent style with minimal code smell. Consistent style makes it easier
for new contributors to follow the code, makes the code easier to maintain, and
helps keep all of us honest when following best-practices. Automatically
checking the code style can reduce the burden of the maintainer in reviewing
pull requests and ensures that the checks are always run.

### pytest-flake8
* Install pytest-flake8 with `conda install pytest-flake8`
* Finds all `.py` files and runs the checks against them.

### Discuss additional flake8 plugins
* pytest-flake8 will run any additional flake plugins it finds. Here are some
  of our favorites:

  - flake8-builtins!=1.4.0
  - flake8-comprehensions
  - flake8-copyright
  - flake8-docstrings
  - flake8-import-order
  - flake8-mutable
  - flake8-pep3101
  - flake8-print
  - flake8-quotes

### Add to Travis config
* Add to the pip install `pytest-flake8  flake8-docstrings flake8-import-order`  
* In the travis config file add the `--flake8` option to the pytest call.

### Running locally
* Always a good idea to run locally to save time!
* We have failures! Let's fix some.

### Supressing warnings
* While rules are great, some of them are more restrictive that we'd like. We
  need to add some rules in `setup.cfg` to modify our flake setup (or create
  `setup.cfg` in the project root if you don't already have one).
* First, let's add a rule to extend the maximum line length - the default of
  79 characters. It's a bit restrictive and in our opinion excessively
  limiting. Add these lines to `setup.cfg` and rerun

```
[flake8]
max-line-length = 95
```

* Sometimes there are flake rules that we don't necessarily agree with either.
  They can be ignored in all files by adding them to the ignore list.

```  
[flake8]
ignore = F403
max-line-length = 95
```

**Activity**
Fix the flake failures, but don't worry about fixing the F403 issues in
`plots/__init__.py`.

**Solution**
* Fix the missing newline in imports in `calc/met.py`
* Fix the whitespace issues in `calc/tests/test_met.py`
* Add a docstring to the plots `__init__.py`

```python
"""This module contains a variety of plotting functions."""
```

* Add a docstring to `plots/special_plot.py`

```python
"""Make a random plot of some size for science.

Makes a random plot of num_points and colored randomly. While this probably
sounds silly, it sometimes shows more patterns that some real dataself.

Parameters
----------
num_points : integer
    The number of random points to plot on the graph.
seed : integer, optional
    Seed value for the random number generator for reproducible plots.

Returns
-------
matplotlib.figure.Figure : figure object
matplotlib.axes._subplots.AxesSubplot : axes

"""
```
