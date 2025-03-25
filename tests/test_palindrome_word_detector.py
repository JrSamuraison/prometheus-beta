import pytest
from src.palindrome_word_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("hello level world") == True
    assert contains_palindrome_word("python 121 code") == True
    assert contains_palindrome_word("radar is here") == True
    assert contains_palindrome_word("A man a plan a canal panama") == True

    # Test cases without palindrome words
    assert contains_palindrome_word("hello world") == False
    assert contains_palindrome_word("no palindromes") == False
    assert contains_palindrome_word("") == False

    # Test cases with mixed content
    assert contains_palindrome_word("hello 123 racecar world") == True
    assert contains_palindrome_word("Able was I ere I saw Elba") == True

    # Test cases with special characters
    assert contains_palindrome_word("hello, world! radar.") == True
    assert contains_palindrome_word("test@#$% case") == False

    # Test case sensitivity
    assert contains_palindrome_word("Madam") == True
    assert contains_palindrome_word("LEVEL test") == True

    # Test minimum length (should be more than 1 character)
    assert contains_palindrome_word("a b c") == False