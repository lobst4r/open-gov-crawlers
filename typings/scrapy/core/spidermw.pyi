"""
This type stub file was generated by pyright.
"""

from scrapy.middleware import MiddlewareManager

"""
Spider Middleware manager

See documentation in docs/topics/spider-middleware.rst
"""
def _isiterable(possible_iterator):
    ...

class SpiderMiddlewareManager(MiddlewareManager):
    component_name = ...
    @classmethod
    def _get_mwlist_from_settings(cls, settings):
        ...
    
    def _add_middleware(self, mw):
        ...
    
    def scrape_response(self, scrape_func, response, request, spider):
        ...
    
    def process_start_requests(self, start_requests, spider):
        ...
    


