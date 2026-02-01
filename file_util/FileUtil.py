"""File utility module for Robot Framework operations."""

from robot.api.deco import keyword


class FileUtil:
    """Provides file operations for Robot Framework automation."""

    @keyword("Read File")
    def read_file(self, file_path):
        """
        Reads the content of a file and returns it as a string.
        
        Args:
            file_path (str): The path to the file to read.
            
        Returns:
            str: The complete content of the file.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If the file cannot be read.
            
        Example:
            | ${content}= | Read File | path/to/file.txt |
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
