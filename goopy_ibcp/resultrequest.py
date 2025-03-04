from dataclasses import dataclass

from goopy_ibcp.error import IBClientError


@dataclass
class RequestResult:
    # request origin
    url: str = ""
    # Decoded message for error
    error = IBClientError.Err_General_Ok
    # Addition error info
    errorMsg = None
    # Client portal Web Error Code
    statusCode = 0
    # Client Portal JSON response string
    json: str = None
    # Raw string (From other formats like XML, etc.)
    raw: str = None
    # Converted Dict
    dict: [] = None
