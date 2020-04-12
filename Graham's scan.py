import math
from matplotlib import pyplot as plt
# points = [(0, 0), (2, 3),  (10, 4), (3, 1),(32, 12), (-1, 3), (4, 3), (1, 3), (4, 9)]
# points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
points = [(0, 2), (-1, -1), (0, 0), (1, -1)]
# points=[(0,0),(1,0),(2,0),(0,2),(2,2),(1,1),(0,0.3)]
P = [-3, -3]


def scatter_plot(coords, convex_hull=None):
    xs, ys = zip(*coords)  # unzip into x and y coord lists
    plt.scatter(xs, ys, c='green')  # plot the data points
    plt.scatter(coords[0][0], coords[0][1], c='red')  # left bottom point

    if convex_hull != None:
        # plot the convex hull boundary, extra iteration at
        # the end so that the bounding line wraps around
        for i in range(1, len(convex_hull)+1):
            if i == len(convex_hull):
                i = 0  # close the figure (paths)
            c0 = convex_hull[i-1]
            c1 = convex_hull[i]
            # build/draw segment [c0; c1]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'magenta')
    plt.show()


def cmp_to_key(mycmp):
    'Convert a cmp-function into a key-function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def distance(p0, p1):
    #     calculates the euclidean distance between 2 points
    y_span = p0[1]-p1[1]
    x_span = p0[0]-p1[0]
    return math.sqrt(y_span**2 + x_span**2)


def direction(p1, p2, p3):
    #   calculates the direction value of an ordered triplet of points in the plane
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def orientation(p1, p2, p3):
    #   calculates the orientation of an ordered triplet of points in the plane
    D = direction(p1, p2, p3)
    if D == 0:
        return 0  # colinear
    elif D > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise


def polar_comparator(p2, p3):
    #     compares two points using the polar angle; used for sorting the points
    D = direction(P, p2, p3)
    if D == 0:
        if distance(P, p3) >= distance(P, p2):
            return - 1
        else:
            return 1
    if (D > 0):
        return -1  # clock
    else:
        return 1  # counterclock


def find_min_y(points):
    #     finds the point having minimum y-coordinate and in case of equality choses the one with minimum x-coordinate
    minx = miny = float('inf')
    mini = -1
    for p in points:
        if p[1] < miny:  # minimum y-coordinate
            miny = p[1]
            P = p
            mini = points.index(p)
    for p in points:
        if p[1] == miny:  # minimum x-coordinate in case of equality
            if p[0] < minx:
                minx = p[0]
                P = p
                mini = points.index(p)
    return P, mini


def graham_scan(points):

    # sort the points (except p0) according to the polar angle
    # made by the line segment with x-axis in anti-clockwise direction
    points.sort(key=cmp_to_key(polar_comparator))

    # let p0 be the point with minimum y-coordinate, or the leftmost such point in case of a tie
    P, index = find_min_y(points)

    # swap p[0] with p[index]
    points[0], points[index] = points[index], points[0]
    print(points)
    n = len(points)
    m = 1  # ignore the first value
    aux = []

    # In case of colinear points, we only keep the maximum value in points array
    for i in range(1, n):
        while i < n-2 and direction(P, points[i], points[i+1]) == 0:
            i += 1
        points[m] = points[i]
        m += 1
    print(points)

    # Delete the duplicate values
    for i in range(n-1):
        if (points[i] == points[i + 1]):
            continue
        else:
            aux.append(points[i])

    if points[n - 1] != aux[len(aux) - 1]:
        aux.append(points[n-1])

    points = aux
    m = len(aux)
    print(points)

    if m < 3:
        print('Convex hull is empty')
        return None

    else:
        # add in stack the points situated on the convex hull
        stack = []
        stack_size = 0
        stack.append(points[0])
        stack.append(points[1])
        stack.append(points[2])
        scatter_plot(points, stack)
        stack_size = 3

        for i in range(3, m):
            # the point is added only if it determines a left-turn (counterclockwise direction)
            while(orientation(stack[stack_size-2], stack[stack_size-1], points[i]) == 2):
                stack.pop()
                stack_size -= 1
                if stack_size < 2:
                    break
            stack.append(points[i])
            scatter_plot(points, stack)
            stack_size += 1
    return stack


print(graham_scan(points))
