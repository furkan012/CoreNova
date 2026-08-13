# test_corenova.py
"""
Tests for CoreNova module.
"""

import unittest
from corenova import CoreNova

class TestCoreNova(unittest.TestCase):
    """Test cases for CoreNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreNova()
        self.assertIsInstance(instance, CoreNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
