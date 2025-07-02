from src.logger import logging
import sys

def error_message_details(error_message, error_details: sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_msg = f'Error occured in Python script [ {file_name} ], line number [ {line_number}, and the error details are [ {str(error_message)} ]'

    return error_msg

class CustomExcetion(Exception):
    def __init__(self, error_message, detailed_error:sys):
        super().__init__(error_message)

        self.error_message = error_message_details(error_message=error_message, error_details=detailed_error)
        logging.info(self.error_message)
    def __str__(self):
        return self.error_message

