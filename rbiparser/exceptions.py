class RBIParserError(Exception):
    """Base exception for all rbiparser errors.
    Catch this to handle any error from the library."""
    pass


class DownloadError(RBIParserError):
    """Raised when downloading files from the RBI website fails."""
    pass


class ParseError(RBIParserError):
    """Raised when parsing or converting an Excel/CSV file fails."""
    pass


class ValidationError(RBIParserError):
    """Raised when input arguments or data fail validation."""
    pass


class StorageError(RBIParserError):
    """Raised when reading or writing files to disk fails."""
    pass


class CombineError(RBIParserError):
    """Raised when combining CSV files fails."""
    pass