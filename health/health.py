from robot.api.deco import keyword

class Health:
    @keyword("Health Check")
    def health_check(self):
        """Performs a health check and returns the status."""
        return {"status": "healthy"}