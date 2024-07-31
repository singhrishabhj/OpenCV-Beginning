# Read an image

`cv2.imread(filename, flag)` is a function in OpenCV (cv2) used to read an image from the specified file path.

- **Parameters:**
  - `filename`: The path to the image file.
  - `flag`: Specifies how the image should be read. It can take one of the following values:
    - `cv2.IMREAD_COLOR` (or integer value 1): Loads a color image, ignoring any transparency.
    - `cv2.IMREAD_GRAYSCALE` (or integer value 0): Loads the image in grayscale mode.
    - `cv2.IMREAD_UNCHANGED` (or integer value -1): Loads the image as-is, including the alpha channel if present.

- **Return Value:**
  - Returns a NumPy array representing the loaded image if successful.

This function is fundamental for loading images into OpenCV and is typically used as a starting point for various image processing tasks.


# Display an image

**Syntax:**

`cv2.imshow(window_name, image)`


**Parameters:**
- `window_name`: A string representing the name of the window where the image will be displayed.
- `image`: The image (as a NumPy array) to be displayed in the specified window.

**Return Value:**
- This function does not return anything.

**Notes:**
- `cv2.imshow()` is a function in OpenCV used to display an image in a window specified by `window_name`.
- The window is created when `cv2.namedWindow()` or `cv2.imshow()` with the same `window_name` is called.
- To display multiple images simultaneously, different `window_name` values should be used.

- As display ios shown for few millisecond we have to add the time.

# Wait key to display an image

**Notes on `waitKey()` function in OpenCV:**

The `waitKey()` function in Python OpenCV allows users to display a window for a specified number of milliseconds or until any key is pressed. Here's how it works:

- **Parameters:**
  - **Milliseconds:** If a positive integer is passed (e.g., `cv2.waitKey(5000)`), it waits for the specified time (in milliseconds) before destroying the window.
  - **0:** If `0` is passed (e.g., `cv2.waitKey(0)`), the function waits indefinitely until any key is pressed.
  - **Returns:** The function returns the ASCII value of the key pressed (if any) or `-1` if no key is pressed before the specified time elapses.

**Examples:**

1. **Display image with a time limit:**
   ```python
   import cv2
  
   # Read the image
   img = cv2.imread("gfg_logo.png")
  
   # Display the image
   cv2.imshow('gfg', img)
  
   # Wait for 5000 milliseconds (5 seconds)
   cv2.waitKey(5000)
   ```

2. **Display image until key pressed:**
   ```python
   import cv2
  
   # Read the image
   img = cv2.imread("gfg_logo.png")
  
   # Display the image
   cv2.imshow('gfg', img)
  
   # Wait indefinitely until any key is pressed
   cv2.waitKey(0)
   ```

In both examples, `cv2.waitKey()` is used after `cv2.imshow()` to display the image and wait either for a specified time or until a key is pressed. These functions are commonly used in OpenCV applications for interactive image display and processing.

# Save an image in a form of file(saved in memory)

### OpenCV-Python `cv2.imwrite()` Method

**Overview:**
- OpenCV-Python is a Python library used for computer vision tasks.
- `cv2.imwrite()` is used to save images to storage devices like your computer's disk.
- It saves the image with a specified filename and format in the current working directory.

**Syntax:**
```python
cv2.imwrite(filename, image)
```

**Parameters:**
- `filename`: A string that specifies the name of the file where the image will be saved. It should include the file extension like `.jpg`, `.png`, etc. (This will be provide by the you)
- `image`: The image data that you want to save. It's typically loaded using `cv2.imread()`.

**Return Value:**
- Returns `True` if the image was saved successfully, otherwise `False`.

**Example:**

```python code
# Importing necessary libraries
import cv2
import os

# Path to the image and directory where we want to save
image_path = r'C:\Users\Rajnish\Desktop\anyFileNames\filess.png'
directory = r'C:\Users\Rajnish\Desktop\anyFileNames'

# Read the image using cv2.imread()
img = cv2.imread(image_path)

# Change current directory to specified directory
os.chdir(directory)

# Print files and directories before saving
print("Files before saving:")
print(os.listdir(directory))

# Define the filename for saving
filename = 'savedImage.jpg'

# Save the image using cv2.imwrite()
cv2.imwrite(filename, img)

# Print files and directories after saving
print("Files after saving:")
print(os.listdir(directory))

print('Image saved successfully')
```

**Output:**
```
Files before saving:
['filess.png']
Files after saving:
['filess.png', 'savedImage.jpg']
Image saved successfully
```

**Explanation:**
- **Import Libraries**: We import `cv2` for image processing and `os` for handling file operations.
- **Read Image**: Using `cv2.imread()`, we load the image from `image_path`.
- **Set Directory**: Change the current working directory to `directory` where we want to save the image.
- **Save Image**: Using `cv2.imwrite()`, we save the image as `'savedImage.jpg'`.
- **Verify**: We print the list of files before and after saving to confirm that `'savedImage.jpg'` has been added.

This method is crucial when working with images in computer vision applications, allowing you to save processed images conveniently.


***
ord() -> The ord() function in Python converts a single character into its Unicode code point, which is an integer representing the character.