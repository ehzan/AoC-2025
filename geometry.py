def orientation(p, q, r):  # Returns: 0: collinear, -1: clockwise, 1: counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
        (q[0] - p[0]) * (r[1] - q[1])
    return (val > 0) - (val < 0)


def on_segment(p, q, r):  # Checks if point q lies on segment pr assuming p,q,r are collinear
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))


def segments_intersect(seg1, seg2):
    (p1, q1), (p2, q2) = seg1, seg2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:  # General case
        return True

    # Special cases: collinear + lying on segment
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False
