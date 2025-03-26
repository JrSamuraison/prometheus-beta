import pytest
from src.custom_stack import CustomStack

def test_custom_stack_initialization():
    """Test stack initialization."""
    stack = CustomStack()
    assert stack.is_empty() is True
    assert len(stack) == 0

def test_push_and_pop():
    """Test push and pop operations."""
    stack = CustomStack()
    stack.push(5)
    assert len(stack) == 1
    assert stack.pop() == 5
    assert stack.is_empty() is True

def test_push_multiple_items():
    """Test pushing multiple items of different types."""
    stack = CustomStack()
    test_items = [1, 'hello', [1, 2, 3], {'key': 'value'}, 3.14]
    
    for item in test_items:
        stack.push(item)
    
    assert len(stack) == len(test_items)
    
    # Check items are popped in reverse order
    for item in reversed(test_items):
        assert stack.pop() == item

def test_peek():
    """Test peek operation."""
    stack = CustomStack()
    stack.push(42)
    assert stack.peek() == 42
    assert len(stack) == 1  # peek should not remove the item

def test_stack_capacity():
    """Test stack capacity limit."""
    stack = CustomStack(capacity=3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    with pytest.raises(OverflowError):
        stack.push(4)

def test_empty_stack_exceptions():
    """Test exceptions for operations on empty stack."""
    stack = CustomStack()
    
    with pytest.raises(IndexError):
        stack.pop()
    
    with pytest.raises(IndexError):
        stack.peek()

def test_stack_length():
    """Test stack length after various operations."""
    stack = CustomStack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    
    stack.pop()
    assert len(stack) == 1
    
    stack.pop()
    assert len(stack) == 0
    assert stack.is_empty() is True