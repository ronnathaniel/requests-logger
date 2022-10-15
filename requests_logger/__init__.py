import requests
import requests_logger


__all__ = []
__author__ = 'Lama Jan'


for patchable_func in requests_logger.patchable_funcs:
    requests_func = getattr(requests, patchable_func)
    patched_func = requests_logger.logging_wrapper(requests_func)
    setattr(requests, patchable_func, patched_func)
