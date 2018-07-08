# Sphinx

## Objectives

- Learn what is Sphinx
- Set up Sphinx for our project
- Use sphinx to automatically generate API documentation
- Build HTML documentation

**Duration: 45 minutes**

### What is Sphinx?

- Documentation generation system
- Uses Restructured Text for marking up text
- Big features:
    - Multi-document support
    - Automatic docstring gathering and parsing

### Configure sphinx

- Create `docs/` subdirectory
- Starting point: sphinx-quickstart
- What did we get?
    - Makefile(s)
    - Generated source: `conf.py`, `index.rst`

### Build docs locally

- How do we use this? `make html`
- Open `docs/_build/index.html`
- Let's clean up `index.rst` and add some text about us:

```rst
Hugs
====

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Hugs (Hugely Useful Geoscience Stuff) is a library of calculations for geophysics
and meteorology.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

- Rebuild
- Can add one section lower in priority with `----`

```rst
License
-------
```

- Can also link with:

```rst
`license file <https://raw.githubusercontent.com/jrleeman/SettingUpOpenSource/master/LICENSE>`_
```

- Let's add a section on our license, with a link to the license file.
- We can also reference another file by listing it under the `toctree` above

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   CONTRIBUTING
```

- Add a file with a contributor's guide

### Including docstrings in HTML docs

- Add `api.rst`:

```rst
.. _api:

The HUGS API
############

.. autofunction:: hugs.calc.get_wind_speed

```

- Add `api` to `index.rst`
- Rebuild
- Add `'sphinx.ext.napoleon'` to `extensions`
- Rebuild
- Exercise: Add the other functions to `api.rst`. Add separate section headers for the different modules and/or types of calculations.

### Resources

- [Sphinx Documentation](http://www.sphinx-doc.org/en/master/)
- [Restructured Text Documentation](http://docutils.sourceforge.net/rst.html)
- [Restructured Text Primer](http://docutils.sourceforge.net/docs/user/rst/quickstart.html)