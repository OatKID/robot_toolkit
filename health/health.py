from robot.api.deco import keyword

@keyword("Health Check")
def health_check():
    """Performs a health check and returns the status."""
    return {"status": "healthy"}