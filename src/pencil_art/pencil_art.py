import cv2

def image_to_sketch(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (21, 21), sigmaX=0, sigmaY=0)

    inverted_blur = cv2.bitwise_not(blurred_image)

    sketch = cv2.divide(gray_image, 255 - inverted_blur, scale=256)

    cv2.imwrite(output_image_path, sketch)
    print(f"Sketch saved at: {output_image_path}")