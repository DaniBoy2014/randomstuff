"""Start the Dungouns Builder app:   python run_builder.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder.app import main

if __name__ == '__main__':
    main()
