"""Health check module for Robot Framework."""

from robot.api.deco import keyword


class Health:
    """Provides health check operations for Robot Framework automation."""

    @keyword("Health Check")
    def health_check(self):
        """
        Performs a health check and returns the status.
        
        Returns:
            dict: A dictionary containing the health status.
                  Example: {"status": "healthy"}
                  
        Example:
            | ${status}= | Health Check |
            | Should Be Equal | ${status}[status] | healthy |
        """
        return {"status": "healthy"}