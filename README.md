# Robot Toolkit

A comprehensive toolkit providing utilities for Robot Framework automation, including file utilities and health checks.

## Features

- **File Utilities**: Read and manipulate files with ease
- **Health Checks**: Monitor system health status
- **Robot Framework Integration**: Seamlessly integrates with Robot Framework as custom keywords

## Installation

```bash
pip install robot-toolkit
```

### Development Installation

```bash
git clone https://github.com/yourusername/robot-toolkit.git
cd robot-toolkit
pip install -e ".[dev]"
```

## Usage

### FileUtil - Reading Files

```python
from robot_toolkit.file_util import FileUtil

file_util = FileUtil()
content = file_util.read_file("path/to/file.txt")
print(content)
```

### Health Check

```python
from robot_toolkit.health import Health

health = Health()
status = health.health_check()
print(status)  # {"status": "healthy"}
```

### Using with Robot Framework

In your Robot Framework test files:

```robot
*** Settings ***
Library    robot_toolkit.file_util.FileUtil
Library    robot_toolkit.health.Health

*** Test Cases ***
Read File Content
    ${content}=    Read File    path/to/file.txt
    Log    ${content}

Check System Health
    ${status}=    Health Check
    Should Be Equal    ${status}[status]    healthy
```

## Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=robot_toolkit
```

## Project Structure

```
robot_toolkit/
├── file_util/          # File utility module
│   ├── __init__.py
│   └── FileUtil.py
├── health/             # Health check module
│   ├── __init__.py
│   └── health.py
├── test/               # Unit tests
│   ├── __init__.py
│   ├── file_util_test.py
│   └── health_test.py
├── main.py
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Requirements

- Python >= 3.10
- Robot Framework >= 7.4.1

## Support

For support, please open an issue on [GitHub Issues](https://github.com/yourusername/robot-toolkit/issues).
