import pathlib

# function to return the file extension
class ExtractFileExtension(object):
    def extension_extract(filename):
        file_extension = pathlib.Path(filename).suffix
        
        return file_extension
