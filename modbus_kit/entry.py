import sys
import argparse
import logging

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

logging.basicConfig(
  format = '%(asctime)s:%(levelname)s:%(message)s',
  datefmt = '%m/%d/%Y %I:%M:%S %p',
  level = logging.DEBUG
)

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    
    # Creating argument parser
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    parser.add_argument('--version', action='version', version='%(prog)s v1.0', help='show version number and exit')
    parser.add_argument('--config-file', type=str, help='path to configuration file')

    # Parsing command-line arguments
    args = parser.parse_args()

    # Setting up logger format
    formatter = logging.Formatter('%(asctime)s:%(module)s:%(levelname)s:%(message)s', '%Y-%m-%d %H:%M:%S')

    # Setting up logger with name
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()

    # Setting up console_handler log level using argument
    # Print debug trace only with --debug flag
    if args.debug:
        console_handler.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)

    # Setting up console_handler's formatter
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Setting up file_debug_handler to store debug level logs
    file_debug_handler = logging.FileHandler('debug.log')
    file_debug_handler.setLevel(logging.DEBUG)
    file_debug_handler.setFormatter(formatter)
    logger.addHandler(file_debug_handler)

    # Setting up file_error_handler to store error level logs
    file_error_handler = logging.FileHandler('error.log')
    file_error_handler.setLevel(logging.ERROR)
    file_error_handler.setFormatter(formatter)
    logger.addHandler(file_error_handler)

    # Displaying a debug message
    logger.debug("Program entry point")

    app = QApplication(sys.argv)
    wnd_main = QMainWindow()
    wnd_main.show()

    app.exec_()

if __name__ == "__main__":
    main()