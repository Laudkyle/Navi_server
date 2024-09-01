import xml.etree.ElementTree as ET


def parse_gpx(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    namespace = {'gpx': 'http://www.topografix.com/GPX/1/1'}
    tracks = {}
    
    for trk in root.findall('.//gpx:trk', namespace):
        name = trk.find('gpx:name', namespace).text
        points = []
        for trkpt in trk.findall('.//gpx:trkpt', namespace):
            lat = float(trkpt.get('lat'))
            lon = float(trkpt.get('lon'))
            points.append((lat, lon))
        tracks[name] = points
    
    return tracks


def path(destination):
    gpx_file = 'path.gpx' 
    tracks = parse_gpx(gpx_file)
    
    selected_track = str(destination)
    
    if selected_track in tracks:
        # Extract coordinates and store in a list of tuples
        coordinates = tracks[selected_track]
        coordinates_list = [(lat, lon) for lat, lon in coordinates]
    return coordinates_list