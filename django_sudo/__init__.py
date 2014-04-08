"""
django_sudo
~~~~~~~~~~~

:copyright: (c) 2014 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django_sudo').version
except Exception as e:  # pragma: no cover
    VERSION = 'unknown'
