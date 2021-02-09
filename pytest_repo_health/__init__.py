"""
Plugin configures pytest to run repo health checks on a code repository.
Plugin takes care of gathering checks, running checks,
and outputting report based on data gathered during checks.
"""
from typing import Union

__version__ = "2.1.0"


def health_metadata(parent_path: list, output_keys: dict):
    """
    Make a decorator that attaches metadata to the target function.

    ``output_keys`` is a dictionary that documents the output keys of the checker.
    Each key is a key-path into the ``all_results`` dictionary, relative to ``parent_path``.
    If the key is a string, it is appended to the parent path,
    otherwise it extends the parent path.
    The ``parent_path``, then, is just a list of strings that is the prefix
    of all the output keys that are generated by the checker.

    Each output-key value is a dictionary containing documentation of that key
    under the key ``'doc'``.
    """
    # Build full path for each output key, based on the parent path.
    expanded_output_keys = {}
    for k, v in output_keys.items():
        # String key equivalent to a path of just one element
        key_more = [k] if isinstance(k, str) else list(k)
        key_path = tuple(parent_path + key_more)
        expanded_output_keys[key_path] = v

    def health_metadata_decorator(func):
        """Add metadata to function documenting the output keys it generates."""
        func.__dict__['pytest_repo_health'] = {
            'output_keys': expanded_output_keys
        }
        return func
    return health_metadata_decorator


def add_key_to_metadata(output_key: Union[str, tuple]):
    """
    Designed for checks which only define one key

    The decorator will assume the docstring for function is the docstring for key
    and will add this info into func.__pytest_repo_health__

    Warning: output_key has to be hashable, currectly assumed to be a tuple with each level listed:
    key = (first_key, second_key, final_key)
    """
    # Build full path for each output key, based on the parent path.

    def health_metadata_decorator(func):
        """Add metadata to function documenting the output keys it generates."""
        final_output_key = tuple([output_key]) if isinstance(output_key, str) else output_key
        func.__dict__['pytest_repo_health'] = {
            'output_keys': {final_output_key:func.__doc__.strip()}
        }
        return func
    return health_metadata_decorator
