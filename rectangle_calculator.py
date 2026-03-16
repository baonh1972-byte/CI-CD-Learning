# Module: rectangle_calculator.py
"""
This module provides functions for calculating the area of a rectangle.
"""

def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    area = length * width
    return area

if __name__ == "__main__":
    # This block will only execute when the script is run directly
    length = 5.0
    width = 10.0
    area = calculate_area(length, width)
    print(f"The area of the rectangle is: {area}")