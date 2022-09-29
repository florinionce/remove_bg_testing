import os
import cv2
import numpy as np


files = os.listdir("input")

def create_dir_of_not_exits(path):
  isExist = os.path.exists(path)
  if not isExist:
    os.makedirs(path)


def first_method(file_name):
  file_path = "input/" + file_name
  output_file_path = "output/opencv/first_method/" + file_name
  originalImage = cv2.imread(file_path)
  grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

  ## Threshold
  _, threshedImage = cv2.threshold(grayscaleImage, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

  ## Find the contours with biggest area
  contours, _ = cv2.findContours(threshedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  maxContour = max(contours, key=cv2.contourArea)

  ## Create mask
  mask = np.zeros(originalImage.shape[:2], np.uint8)
  cv2.drawContours(mask, [maxContour], -1, 255, -1)

  ## Copy the croped image to a white canvas
  destinationImage = np.zeros(originalImage.shape[:3], np.uint8)
  height = originalImage.shape[:2][1]
  destinationImage[:, 0:height] = (255, 255, 255)

  locations = np.where(mask != 0)
  destinationImage[locations[0], locations[1]] = originalImage[locations[0], locations[1]]

  ## Save
  cv2.imwrite(output_file_path, destinationImage)

def second_method(file_name):
  file_path = "input/" + file_name
  output_file_path = "output/opencv/second_method/" + file_name

  img = cv2.imread(file_path)
  hh, ww = img.shape[:2]

  # threshold on white
  # Define lower and uppper limits
  lower = np.array([200, 200, 200])
  upper = np.array([255, 255, 255])

  # Create mask to only select black
  thresh = cv2.inRange(img, lower, upper)

  # apply morphology
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
  morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

  # invert morp image
  mask = 255 - morph

  # apply mask to image
  result = cv2.bitwise_and(img, img, mask=mask)


  # save results
  cv2.imwrite(output_file_path, result)


create_dir_of_not_exits('output/opencv')
create_dir_of_not_exits('output/opencv/first_method')
create_dir_of_not_exits('output/opencv/second_method')

for file_name in files:
  first_method(file_name)
  second_method(file_name)
