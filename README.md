python-mbus
===========

Added send_custom_text and tests for that and secondary addressing. Needs my fork of libmbus to work. I used sensenode instead of master because it seems to have addressed some issues with the original, and the original is abandoned. // Jouzer

Python wrapper for [libmbus](http://www.rscada.se/libmbus) ([source](https://github.com/rscada/libmbus))

* installation: run ```python setup.py install```
* tests: run ```py.test```
    * please adjust the serial device in pytest.ini
    * to only run tests involving the serial device, run ```py.test -m serial```

License
=======

This software is licensed under the [BSD license](http://opensource.org/licenses/BSD-3-Clause). 
