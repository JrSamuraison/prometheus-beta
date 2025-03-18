import pytest
from src.sequence_reconstruction import min_reconstruction_edits

def test_identical_sequences():
    """Test when sequences are identical"""
    original = [1, 2, 3, 4, 5]
    modified = [1, 2, 3, 4, 5]
    assert min_reconstruction_edits(original, modified) == 0

def test_empty_sequences():
    """Test empty sequences"""
    assert min_reconstruction_edits([], []) == 0
    assert min_reconstruction_edits([], [1, 2, 3]) == 3
    assert min_reconstruction_edits([1, 2, 3], []) == 3

def test_single_element_sequences():
    """Test sequences with single elements"""
    assert min_reconstruction_edits([1], [2]) == 1
    assert min_reconstruction_edits([1], [1]) == 0

def test_different_length_sequences():
    """Test sequences of different lengths"""
    original = [1, 2, 3]
    modified = [1, 2, 3, 4, 5]
    assert min_reconstruction_edits(original, modified) == 2

    original = [1, 2, 3, 4, 5]
    modified = [1, 2, 3]
    assert min_reconstruction_edits(original, modified) == 2

def test_complex_transformations():
    """Test more complex sequence transformations"""
    original = [1, 2, 3, 4, 5]
    modified = [2, 4, 6]
    assert min_reconstruction_edits(original, modified) == 4

def test_similar_but_not_identical_sequences():
    """Test sequences that require multiple edits"""
    original = [1, 2, 3, 4, 5]
    modified = [1, 3, 5, 6]
    assert min_reconstruction_edits(original, modified) == 2

def test_completely_different_sequences():
    """Test completely different sequences"""
    original = [1, 2, 3]
    modified = [4, 5, 6]
    assert min_reconstruction_edits(original, modified) == 3

def test_partially_overlapping_sequences():
    """Test sequences with partial overlap"""
    original = [1, 2, 3, 4, 5]
    modified = [3, 4, 5, 6, 7]
    assert min_reconstruction_edits(original, modified) == 3