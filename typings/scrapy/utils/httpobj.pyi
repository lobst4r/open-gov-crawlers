"""
This type stub file was generated by pyright.
"""

import weakref

"""Helper functions for scrapy.http objects (Request, Response)"""
_urlparse_cache = weakref.WeakKeyDictionary()
def urlparse_cached(request_or_response):
    """Return urlparse.urlparse caching the result, where the argument can be a
    Request or Response object
    """
    ...

