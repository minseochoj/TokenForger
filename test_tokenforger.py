# test_tokenforger.py
"""
Tests for TokenForger module.
"""

import unittest
from tokenforger import TokenForger

class TestTokenForger(unittest.TestCase):
    """Test cases for TokenForger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenForger()
        self.assertIsInstance(instance, TokenForger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenForger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
