fs.wrapcifs
===========

``fs.wrapcifs`` is a PyFileSystem2 wrapper which makes path lookups case insensitive.

Supported Python versions
-------------------------

- Python 3.11

Usage
-----

.. code:: python

    >>> from fs.wrapcifs import WrapCaseInsensitive
    >>> from fs.zipfs import ReadZipFS

    >>> WrapCaseInsensitive(ReadZipFS('example.zip')).getinfo('abc').name == 'ABC'
    ....
    True

License
-------

This module is published under the MIT license.