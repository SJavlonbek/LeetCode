def flipAndInvertImage(image):
    return [[1 if element == 0 else 0 for element in item[::-1] ] for item in image]