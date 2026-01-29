import pytest

from health import health_check

def test_health_check():
    result = health_check()
    assert result == {"status": "healthy"}