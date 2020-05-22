"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

class BaseDupeFilter(object):
    @classmethod
    def from_settings(cls, settings):
        ...
    
    def request_seen(self, request):
        ...
    
    def open(self):
        ...
    
    def close(self, reason):
        ...
    
    def log(self, request, spider):
        ...
    


class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""
    def __init__(self, path: Optional[Any] = ..., debug: bool = ...):
        self.file = ...
        self.fingerprints = ...
        self.logdupes = ...
        self.debug = ...
        self.logger = ...
    
    @classmethod
    def from_settings(cls, settings):
        ...
    
    def request_seen(self, request):
        ...
    
    def request_fingerprint(self, request):
        ...
    
    def close(self, reason):
        ...
    
    def log(self, request, spider):
        ...
    


