def find_overlap(p1, l1, p2, l2):
    highest_start_point = max(p1, p2)
    lowest_end_point = min(p1+l1, p2+l2)

    if lowest_end_point < highest_start_point:
        return (0, 0)

    overlap_len = lowest_end_point - highest_start_point
    overlap_start_point = highest_start_point

    return (overlap_start_point, overlap_len)

def find_intersection(rectangle1, rectangle2):
    x1, y1 = rectangle1['left_x'], rectangle1['bottom_y']
    x2, y2 = rectangle2['left_x'], rectangle2['bottom_y']
    w1, h1 = rectangle1['width'], rectangle1['height']
    w2, h2 = rectangle2['width'], rectangle2['height']

    rectangle = {}
    rectangle['height'] = 0
    rectangle['width'] = 0

    x_overlap = find_overlap(x1, w1, x2, w2)
    y_overlap = find_overlap(y1, h1, y2, h2)

    if not x_overlap[1] or not x_overlap[1]:
        return None
    else:
        return {
           'left_x': x_overlap[0],
            'bottom_y': y_overlap[0],
            'width': x_overlap[1],
            'height': y_overlap[1],
        }

rectangle1 = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 0,

    # width and height
    'width': 10,
    'height': 10,

}

rectangle2 = {

    # coordinates of bottom-left corner
    'left_x': 2,
    'bottom_y': 2,

    # width and height
    'width': 4,
    'height': 4,

}

print(find_intersection(rectangle1, rectangle2))


