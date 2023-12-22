
import os 
from PIL import Image #pillow module
import numpy as np
import random
from shutil import copyfile


def load_many_images_for_binary_classification(numImgsToLoad, rootFolder):
    
    """
    binary classification either 0 or 1
    """
    imageData = []
    labels = []
    # Loop through each folder
    labelCount = 0
    arrFolderName = []
    for folder_name in os.listdir(rootFolder):
        arrFolderName.append(folder_name)
        folder_path = os.path.join(rootFolder, folder_name)
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # List all files in the folder
            all_files = os.listdir(folder_path)
    
            # Randomly select 50 images (if available)
            selected_files = random.sample(all_files, min(numImgsToLoad, len(all_files)))

            for imgName in selected_files:
                img = load_image(f"{folder_path}/{imgName}")
                imgPixels = image_to_pixels(img)
                imageData.append(imgPixels)
                labels.append(labelCount)
            labelCount += 1
            if labelCount > 1:
                break
    print("folders names",arrFolderName)
    return np.array(imageData), np.array(labels).reshape(1, -1)




def load_many_images_of_many_different_types(numImgsToLoad, rootFolder):
    
    """
        returns two arrays one of image pixel data of shapes  (# of images, pixel count x, pixel count y, 3),
        and another array of shape (# for image identifier, # of images) 

        # for image identifier means that if its an image of a forest than label it a 1 if its a sea image label
        it a 2 etc.... theses are determined by which folder its in
    """
    imageData = []
    labels = []
    # Loop through each folder
    labelCount = 0
    for folder_name in os.listdir(rootFolder):
        folder_path = os.path.join(rootFolder, folder_name)
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # List all files in the folder
            all_files = os.listdir(folder_path)
    
            # Randomly select 50 images (if available)
            selected_files = random.sample(all_files, min(numImgsToLoad, len(all_files)))

            for imgName in selected_files:
                img = load_image(f"{folder_path}/{imgName}")
                imgPixels = image_to_pixels(img)
                imageData.append(imgPixels)
                labels.append(labelCount)
            labelCount += 1
    return np.array(imageData), np.array(labels).reshape(1, -1)


def image_to_pixels(image):
    pixel_data = np.array(image)
    return pixel_data

def load_image(image_path):
    image = Image.open(image_path)
    return image





def find_and_delete_non_size_images(main_folder_path, imageX_size, imageY_size):
  """Finds and deletes images in subfolders of the main folder that are not imageX_size x imageY_size pixels."""

  for root, directories, files in os.walk(main_folder_path):
    for file in files:
      if file.endswith((".jpg", ".jpeg", ".png")):  # Check for common image extensions
        image_path = os.path.join(root, file)
        try:
          with Image.open(image_path) as img:
            width, height = img.size
            if width != imageX_size or height != imageY_size:
              os.remove(image_path)
              print(f"Deleted {image_path} (not 150x150)")
        except (IOError, OSError) as e:
          print(f"Error processing {image_path}: {e}")

# Example usage:
# main_folder_path = "path to folder"  # Replace with your actual path
# find_and_delete_non_150x150_images(main_folder_path)



