import cv2
import os
from natsort import natsorted  # Ensures numerical sorting

# Parameters
image_folder = "scene-0012/_vis"
output_path = "output_video.mp4"
fps = 10

# Get image file paths and sort them
images = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".png"))]
images = natsorted(images)

if not images:
    raise ValueError("No image files found in the specified folder.")

# Read the first image to get frame size
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, _ = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also try 'XVID'
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Write each image to the video
for img_name in images:
    img_path = os.path.join(image_folder, img_name)
    frame = cv2.imread(img_path)
    if frame is None:
        print(f"Warning: Couldn't read image {img_path}, skipping.")
        continue
    video_writer.write(frame)

video_writer.release()
print(f"Video saved to: {output_path}")
