"""
Checks tox.ini format
"""
import re

import pytest
from opynions import get_file_content

module_dict_key = 'tox_ini'


@pytest.fixture
def tox_ini(repo_path):
    """Fixture containing the text content of Makefile"""
    #TODO(jinder): make below work with inputs with both "/" at end and not
    full_path = repo_path + '/tox.ini'
    return get_file_content(full_path)

def check_has_sections(tox_ini, all_results):
    """
    Test to check if makefile has an upgrade target
    """
    required_sections = [r'tox', r'testenv', r'testenv:quality']
    all_results[module_dict_key]['has_section'] = {}
    for section in required_sections:
        regex_pattern = r"\[" + section + r"\]"
        match = re.search(regex_pattern, tox_ini)
        all_results[module_dict_key]['has_section'][section] = False
        if match is not None:
             all_results[module_dict_key]['has_section'][section] = True
