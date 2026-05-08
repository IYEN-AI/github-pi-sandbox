"""Tests for the calculator module."""
import pytest
from calculator import add, subtract, multiply, divide


class TestAddition:
    """Test the add function."""
    
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5
        assert add(-10, -15) == -25
    
    def test_add_mixed_numbers(self):
        assert add(2, -3) == -1
        assert add(-5, 8) == 3
    
    def test_add_with_zero(self):
        assert add(0, 5) == 5
        assert add(10, 0) == 10
        assert add(0, 0) == 0


class TestSubtraction:
    """Test the subtract function."""
    
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    
    def test_subtract_negative_numbers(self):
        assert subtract(-2, -5) == 3
        assert subtract(-10, -3) == -7
    
    def test_subtract_mixed_numbers(self):
        assert subtract(5, -3) == 8
        assert subtract(-5, 8) == -13
    
    def test_subtract_with_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0


class TestMultiplication:
    """Test the multiply function."""
    
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12
        assert multiply(7, 6) == 42
    
    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12
        assert multiply(-5, -2) == 10
    
    def test_multiply_mixed_numbers(self):
        assert multiply(3, -4) == -12
        assert multiply(-5, 6) == -30
    
    def test_multiply_with_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 7) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_with_one(self):
        assert multiply(8, 1) == 8
        assert multiply(1, 9) == 9


class TestDivision:
    """Test the divide function."""
    
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0
        assert divide(7, 2) == 3.5
    
    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5.0
        assert divide(-15, -3) == 5.0
    
    def test_divide_mixed_numbers(self):
        assert divide(10, -2) == -5.0
        assert divide(-15, 3) == -5.0
    
    def test_divide_with_one(self):
        assert divide(8, 1) == 8.0
        assert divide(-8, 1) == -8.0
    
    def test_divide_zero_numerator(self):
        assert divide(0, 5) == 0.0
        assert divide(0, -3) == 0.0
    
    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(-5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)