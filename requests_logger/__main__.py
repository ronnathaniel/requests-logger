
import requests
import logging
import typing


patchable_funcs = ['get', 'post', 'put', 'delete', 'options']


def logging_wrapper(original_function: typing.Callable) -> typing.Callable:
    requests_method = original_function.__name__
    if requests_method not in patchable_funcs:
        return original_function

    def inner_logging_wrapper(*args) -> typing.Any:
        logging.log(
            logging.DEBUG,
            'REQUEST to: {url}'.format(url=args[:1])
        )
        original_result = original_function(*args)
        logging.log(
            logging.DEBUG,
            '{method}: {status}'.format(
                method=requests_method,
                status=original_result.status_code,
            )
        )

        return original_result

    return inner_logging_wrapper


