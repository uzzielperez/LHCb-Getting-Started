import cv2

# Load the image
image_path = 'LHCB PREVIEW-white-bg.jpg'
# image_path = 'LHCbMSokoloff.png'
image = cv2.imread(image_path)

# Define the callback function to display the coordinates
def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")
        # Display the coordinates on the image
        # cv2.putText(image, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2) # (255, 0, 0) = (, G, B)
        cv2.putText(image, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow("Image", image)

# Create a window and set the mouse callback function
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", show_coordinates)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2

# # Load the image
# image_path = 'LHCB PREVIEW-white-bg.jpg'
# image = cv2.imread(image_path)

# # Define the callback function to display the coordinates
# def show_coordinates(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:
#         # Create a copy of the original image to draw on
#         image_copy = image.copy()
        
#         # Get image dimensions
#         height, width, _ = image.shape
        
#         # Define the text and font parameters
#         text = f"Coordinates: ({x}, {y})"
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         font_scale = 0.5
#         font_color = (255, 255, 255)  # White
#         thickness = 1
        
#         # Calculate text size to place it properly at the bottom-right
#         text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
#         text_x = width - text_size[0] - 10  # 10 pixels margin
#         text_y = height - 10  # 10 pixels margin from the bottom
        
#         # Draw the text on the image
#         cv2.putText(image_copy, text, (text_x, text_y), font, font_scale, font_color, thickness)
        
#         # Show the updated image
#         cv2.imshow("Image", image_copy)

# # Create a window and set the mouse callback function
# cv2.imshow("Image", image)
# cv2.setMouseCallback("Image", show_coordinates)

# # Wait until a key is pressed
# cv2.waitKey(0)
# cv2.destroyAllWindows()



