import math

def closest_pair_with_points(points):
    # Sort the points based on their x-coordinate
    points.sort(key=lambda point: point[0])

    # Recursive helper function to find the closest pair
    def closest_pair_rec(points):
        n = len(points)

        # Base case: if there are only two or three points, calculate the distance directly
        if n <= 3:
            min_distance = float('inf')
            closest_points = None
            for i in range(n):
                for j in range(i+1, n):
                    dist = distance(points[i], points[j])
                    if dist < min_distance:
                        min_distance = dist
                        closest_points = [points[i], points[j]]
            return min_distance, closest_points

        # Divide the points into two halves
        mid = n // 2
        left_half = points[:mid]
        right_half = points[mid:]

        # Recursively find the closest pairs in each half
        left_dist, left_points = closest_pair_rec(left_half)
        right_dist, right_points = closest_pair_rec(right_half)

        # Find the minimum distance between points in the two halves
        min_dist = min(left_dist, right_dist)
        closest_points = left_points if left_dist < right_dist else right_points

        # Find points within min_dist from the dividing line
        strip = [point for point in points if abs(point[0] - points[mid][0]) < min_dist]

        # Sort the points in the strip based on their y-coordinate
        strip.sort(key=lambda point: point[1])

        # Compare each point with its neighbors in the strip
        for i in range(len(strip)):
            for j in range(i+1, min(i+8, len(strip))):  # Check at most 7 points ahead
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_points = [strip[i], strip[j]]

        return min_dist, closest_points

    return closest_pair_rec(points)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

if __name__ == '__main__':
    points = [ (1, 3), (4, 5), (5, 1), (2, 0), (3, 4)]
    min_distance, closest_points = closest_pair_with_points(points)
    print("Closest distance:", min_distance)
    print("Closest points:", closest_points)
