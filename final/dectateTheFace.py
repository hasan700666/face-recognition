import face_recognition
from PIL import Image, ImageDraw 

# 1. Load image
img_path = "Picture/images.jpeg"
image = face_recognition.load_image_file(img_path)

# 2. Find faces
face_locations = face_recognition.face_locations(image)
print("Faces found:", face_locations)

# 3. Convert to PIL (so we can draw)
pil_img = Image.fromarray(image)
draw = ImageDraw.Draw(pil_img)

#pil_img.show() 

# 4. Draw red rectangle for every face
for top, right, bottom, left in face_locations:
    draw.rectangle([left, top, right, bottom], outline="red", width=4)


# # 5. Show the result
pil_img.show()          # opens the default image viewer
pil_img.save("with_boxes.jpg")   # optional: save a copy