"""
Given an array of points with integer coordinates (x, y).
Determine if there is a vertical line dividing the points into 2 sets symmetric with respect to this line.

(X5-2023)
"""

points = [
    (0, 2),
    (1, 1),
    (3, 1),
    (4, 2),
]


def is_vert_sym(pts):

    if len(pts) == 0:
        return None
    if len(pts) == 1:
        return True

    # Detect potential candidate (which X coordinate is a candidate in line of symmetry).
    # It will be an AVG x coordinate
    x_mid = sum([p[0] for p in points])/len(pts)
    print(f"{x_mid=}")

    result = True

    for p in pts:

        xp = p[0]
        yp = p[1]
        print(f"({xp}, {yp})")

        # For every point check if there is a symmetric point in array

        # Is point is on the left side from line, check if there is a "symmetric" point on the right side
        if xp < x_mid:
            if (x_mid + (x_mid - xp), yp) not in pts:
                result = False
                break

        # Is point is on the right side from line, check if there is a "symmetric" point on the left side
        elif xp > x_mid:
            if (xp - 2*(xp - x_mid), yp) not in pts:
                result = False
                break

        # Point on the line shouldn't be checked

    return result


if __name__ == '__main__':
    print(is_vert_sym(points))


