# Graham's scan

It is a program written in Python designed to do the Convex Hull of a given a set of points in the plane. The convex hull of the set is the smallest convex polygon that contains all the points of it.

## Describing Graham's scan algorithm
Graham's scan is a method of finding the convex hull of a finite set of points in the plane with time complexity O(n log n). It is named after Ronald Graham, who published the original algorithm in 1972. The algorithm finds all vertices of the convex hull ordered along its boundary. It uses a stack to detect and remove concavities in the boundary efficiently.

## Describing the code
  ### Functions:
  * scatter_plot: plots the data points and draws the segments between points
  * distance: returns the distance between 2 points
  * direction(point1, point2, point3): calculates the euclidean distance between 2 points
  * orientation(point1, points2, points3): calculates the orientation of an ordered triplet of points in the plane
  * polar_comparator: compares two points using the polar angle; used for sorting the points
  * find_min_y: finds the point having minimum y-coordinate and in case of equality choses the one with minimum x-coordinate
  * graham_scan:
    - sort the points (except p0) according to the polar angle made by the line segment with x-axis in anti-clockwise direction
    - let p0 be the point with minimum y-coordinate, or the leftmost such point in case of a tie
    - in case of colinear points, we only keep the maximum value in points array
    - delete the duplicate values
    - add in stack the points situated on the convex hull, the point is added only if it determines a left-turn (counterclockwise direction) 
