import pytest
import math
from src.fibonacci_square_pairs import generate_fibonacci_square_pairs, is_perfect_square

def test_is_perfect_square():
    """Test the perfect square detection function."""
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True
    
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(7) == False
    assert is_perfect_square(-4) == False

def test_generate_fibonacci_square_pairs_basic():
    """Test generating Fibonacci-like sequence with square pair sums."""
    # Test basic cases
    assert generate_fibonacci_square_pairs(1) == [1]
    assert generate_fibonacci_square_pairs(2) == [1, 3]
    
    # Confirm square pair sum property
    seq = generate_fibonacci_square_pairs(5)
    assert len(seq) == 5
    
    # Check that each consecutive pair sum is a perfect square
    for i in range(len(seq) - 2):
        pair_sum = seq[i] + seq[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"

def test_generate_fibonacci_square_pairs_advanced():
    """Test more complex scenarios of square pair sum generation."""
    # Generate multiple sequences and validate
    sequences = [
        generate_fibonacci_square_pairs(3),
        generate_fibonacci_square_pairs(4),
        generate_fibonacci_square_pairs(6)
    ]
    
    for seq in sequences:
        # Verify length and basic generation
        assert len(seq) > 1
        
        # Check square pair sum property
        for i in range(len(seq) - 2):
            pair_sum = seq[i] + seq[i+1]
            assert is_perfect_square(pair_sum), f"Sequence {seq}: Pair sum {pair_sum} is not a perfect square"

def test_generate_fibonacci_square_pairs_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        generate_fibonacci_square_pairs("3")
    
    with pytest.raises(TypeError):
        generate_fibonacci_square_pairs(3.5)
    
    with pytest.raises(ValueError):
        generate_fibonacci_square_pairs(0)
    
    with pytest.raises(ValueError):
        generate_fibonacci_square_pairs(-1)

def test_generate_fibonacci_square_pairs_consistency():
    """Verify that repeated calls produce consistent results."""
    seq1 = generate_fibonacci_square_pairs(5)
    seq2 = generate_fibonacci_square_pairs(5)
    assert seq1 == seq2, "Function should produce consistent results"