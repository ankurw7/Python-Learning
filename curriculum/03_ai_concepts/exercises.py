"""
Module: 03_ai_concepts
Topic: Exercises
Description: Practice problems for AI math and logic.
"""

def exercise_relu(x: float) -> float:
    """
    TODO: Implement the ReLU (Rectified Linear Unit) activation function.
    
    ReLU(x) = max(0, x)
    
    Args:
        x (float): Input value.
        
    Returns:
        float: 0 if x is negative, else x.
    """
    return max(0, x)


def exercise_matrix_add(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    TODO: Implement matrix addition.
    
    Add two 2D lists (matrices) element-wise.
    Assume both matrices have the same dimensions.
    
    Args:
        matrix_a: First matrix.
        matrix_b: Second matrix.
        
    Returns:
        list[list[float]]: The sum of the matrices.
    """
    return [
        [a + b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]


def exercise_euclidean_distance(point_a: tuple[float, float], point_b: tuple[float, float]) -> float:
    """
    TODO: Implement Euclidean distance between two 2D points.
    
    Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    
    Args:
        point_a: (x, y) coordinates of first point.
        point_b: (x, y) coordinates of second point.
        
    Returns:
        float: The distance.
    """
    import math
    dx = point_b[0] - point_a[0]
    dy = point_b[1] - point_a[1]
    return math.sqrt(dx ** 2 + dy ** 2)
