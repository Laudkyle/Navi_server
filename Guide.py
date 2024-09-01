from geopy.distance import great_circle
from math import atan2, degrees, radians, sin, cos

# Function to calculate bearing from one point to another
def calculate_bearing(start_point, end_point):
    start_lat = radians(start_point[0])
    start_lon = radians(start_point[1])
    end_lat = radians(end_point[0])
    end_lon = radians(end_point[1])

    d_lon = end_lon - start_lon
    x = atan2(
        sin(d_lon) * cos(end_lat),
        cos(start_lat) * sin(end_lat) - sin(start_lat) * cos(end_lat) * cos(d_lon)
    )
    bearing = (degrees(x) + 360) % 360
    return bearing

# Function to convert distance to steps
def distance_to_steps(distance_meters, stride_length=0.75):
    return distance_meters / stride_length

# Function to determine the turn command based on angle difference
def get_turn_command(turn_angle):
    if turn_angle < 0:
        turn_angle += 360  # Normalize to 0-360 degrees

    if 0 <= turn_angle < 25:
        return "turn left"
    elif 25 <= turn_angle < 75:
        return "partial left"
    elif 75 <= turn_angle < 105:
        return "forward"
    elif 105 <= turn_angle < 155:
        return "partial right"
    elif 155 <= turn_angle <= 180:
        return "turn right"
    return "forward"  

def guide_user(current_location, waypoints):
    # Assume starting direction is 0 degrees (North)
    current_direction = 0

    for waypoint in waypoints:
        # Calculate bearing and distance to the next waypoint
        target_bearing = calculate_bearing(current_location, waypoint)
        distance = great_circle(current_location, waypoint).meters
        
        # Convert distance to steps
        steps = distance_to_steps(distance)
        
        # Calculate turn angle
        turn_angle = target_bearing - current_direction
        
        # Normalize the angle to be between -180 and 180
        if turn_angle > 180:
            turn_angle -= 360
        elif turn_angle < -180:
            turn_angle += 360
        
        # Get the turn command
        turn_command = get_turn_command(abs(turn_angle))
        
        # Generate final command
        command = f"{turn_command} and walk {int(steps)} steps"
        print(f"Instruction: {command}")
        
        # Update current direction
        current_direction = target_bearing
        
        # Move to next waypoint
        current_location = waypoint

def main():
    current_location = (5.116800, -1.292400)  # Example current location
    waypoints = [
        (5.116716, -1.292261),
        (5.116773, -1.292426),
        (5.116776, -1.292506),
        (5.116794, -1.29258),
        (5.116866, -1.292765),
        (5.116877, -1.292836),
        (5.11694, -1.292963),
        (5.116991, -1.293017),
        (5.117051, -1.293054),
        (5.117072, -1.293078),
        (5.117096, -1.29318),
        (5.117124, -1.293214),
        (5.11716, -1.293238),
        (5.117178, -1.293271),
        (5.117106, -1.293274),
        (5.117069, -1.293293),
        (5.116979, -1.293453)
    ]
    
    guide_user(current_location, waypoints)

if __name__ == "__main__":
    main()
