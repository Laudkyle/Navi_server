from flask import Flask, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)

# Define the folder containing known images
KNOWN_IMAGES_FOLDER = 'known_images'
os.makedirs(KNOWN_IMAGES_FOLDER, exist_ok=True)

@app.route('/verify', methods=['POST'])
def verify_face():
    if 'image' not in request.files:
        return jsonify({'error': 'Image file is required'}), 400
    
    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'Image file is missing'}), 400
    
    # Save the uploaded image
    uploaded_image_path = os.path.join('uploads', 'uploaded_image.jpg')
    os.makedirs('uploads', exist_ok=True)
    image_file.save(uploaded_image_path)

    # Compare uploaded image with known images
    results = []
    for known_image_name in os.listdir(KNOWN_IMAGES_FOLDER):
        known_image_path = os.path.join(KNOWN_IMAGES_FOLDER, known_image_name)
        
        try:
            result = DeepFace.verify(uploaded_image_path, known_image_path)
            if result['verified']:
                results.append({
                    'known_image': known_image_name,
                    'result': result
                })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    if not results:
        return jsonify({'message': 'No match found'}), 404
    
    return jsonify({'matches': results})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)
