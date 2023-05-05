import cv2

# Load the image
img = cv2.imread('image.jpg')

# Get the dimensions of the image
h, w = img.shape[:2]

# Split the image into four quadrants
q1 = img[0:h//2, 0:w//2]
q2 = img[0:h//2, w//2:w]
q3 = img[h//2:h, 0:w//2]
q4 = img[h//2:h, w//2:w]

# Display the quadrants
cv2.imshow('Quadrant 1', q1)
cv2.imshow('Quadrant 2', q2)
cv2.imshow('Quadrant 3', q3)
cv2.imshow('Quadrant 4', q4)



# Wait for user input and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
