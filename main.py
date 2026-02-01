"""Entry point for robot-toolkit package."""

from file_util import FileUtil
from health import Health


def main():
    """Demonstrate the robot-toolkit functionality."""
    print("Robot Toolkit v0.1.0")
    print("-" * 40)
    
    # Demo: Health Check
    print("Running health check...")
    health = Health()
    status = health.health_check()
    print(f"Health Status: {status}")
    
    print("\nRobot Toolkit is ready to use!")


if __name__ == "__main__":
    main()
