import xml.etree.ElementTree as ET

def extract_coordinates_from_file(file_path):
    # Read the XML content from the file with appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_data = file.read()
    
    root = ET.fromstring(xml_data)
    coordinates = []

    # Iterate over the elements to find LatLngData
    for latlngdata in root.findall('LatLngData'):
        # Extract text and split by comma
        lat_lng = latlngdata.text.split(',')
        # Convert to float and create a tuple
        latitude = float(lat_lng[0])
        longitude = float(lat_lng[1])
        coordinates.append((latitude, longitude))
    
    return coordinates


# Path to the XML file
file_path = 'coordinates.txt'

# Extract coordinates from the file
coordinates_list = extract_coordinates_from_file(file_path)

# Print the result
print(coordinates_list)
