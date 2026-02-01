from robot.api.deco import keyword

class FileUtil:
    @keyword("Read File")
    def read_file(self, file_path):
        """Reads the content of a file and returns it as a string."""
        with open(file_path, 'r') as file:
            return file.read()