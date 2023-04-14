"""Programme to count the sum of numbers in a time string"""
import pytest


def sum_current_time(time_str: str) -> int:
    """Sums up the numbers in the input time string, which should be in the format HH:MM:SS."""

    hour_min_sec_split = time_str.split(":")
    count = 0
    if len(hour_min_sec_split) != 3:
        raise ValueError("Input string must be in the format HH:MM:SS")
    try:
        hours, minutes, seconds = map(int, hour_min_sec_split)
        print(hours)
    except ValueError:
        raise ValueError("Input string must only contain integers")
    if hours < 0 or minutes < 0 or seconds <0:
        raise ValueError("Input cannot contain negative numbers")
    for num in hour_min_sec_split:
        str_to_int = int(num)
        count += str_to_int

    return count


def test_large_input():
    """test 1"""
    time_str = "20:59:59"
    assert sum_current_time(time_str) == 138

def test_midnight():
    """test 2"""
    time_str = "00:00:00"
    assert sum_current_time(time_str) == 0

def test_no_seconds():
    """test 3"""
    time_str = "12:34"
    with pytest.raises(ValueError):
        assert sum_current_time(time_str) == "Input string must be in the format HH:MM:SS"

def test_negative_input():
    """test 4"""
    time_str = "-1:20:10"
    with pytest.raises(ValueError):
        sum_current_time(time_str)

def test_float_input():
    """test 5"""
    time_str = "2.5:45:30"
    with pytest.raises(ValueError):
        sum_current_time(time_str)

def test_empty_input():
    """test 6"""
    time_str = ""
    with pytest.raises(ValueError):
        sum_current_time(time_str)



print(sum_current_time("01:02:03"))


