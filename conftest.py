"""pytest fixtures for simplified testing."""
from __future__ import absolute_import
import pytest
pytest_plugins = ['aiida.manage.tests.pytest_fixtures']


@pytest.fixture(scope='function', autouse=True)
def clear_database_auto(clear_database):  # pylint: disable=unused-argument
    """Automatically clear database in between tests."""
    pass


@pytest.fixture(scope='function')
def quantumespresso_magnetic_code(aiida_local_code_factory):
    """Get a quantumespresso_magnetic code.
    """
    quantumespresso_magnetic_code = aiida_local_code_factory(
        executable='diff', entry_point='quantumespresso_magnetic')
    return quantumespresso_magnetic_code
