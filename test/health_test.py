import pytest


def test_health_check():
    from health.health import Health
    health = Health()
    status = health.health_check()
    assert status == {"status": "healthy"}