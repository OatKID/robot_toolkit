# Contributing to Robot Toolkit

Thank you for your interest in contributing to Robot Toolkit! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/robot-toolkit.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Install in development mode: `pip install -e ".[dev]"`

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `pytest`
4. Format code: `black robot_toolkit/`
5. Lint code: `ruff check robot_toolkit/`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use `black` for code formatting
- Use `ruff` for linting
- Write docstrings for all functions and classes
- Keep lines under 100 characters

## Testing

- Write tests for all new features
- Ensure all tests pass before submitting a PR
- Aim for > 80% code coverage
- Use pytest for all tests

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in the imperative mood (e.g., "Add", "Fix", "Update")
- Keep the first line under 50 characters
- Add more detailed explanations if needed

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Ensure the PR description clearly describes the changes
3. Link any related issues
4. Wait for CI/CD checks to pass
5. Request review from maintainers

## Reporting Bugs

- Use the GitHub Issues tracker
- Provide a clear description of the bug
- Include steps to reproduce
- Include your Python version and environment details

## Feature Requests

- Use the GitHub Issues tracker with a `feature-request` label
- Describe the use case and expected behavior
- Consider implementation approach if possible

## Questions?

Feel free to open an issue with the `question` label if you're unsure about something.

Thank you for contributing!
