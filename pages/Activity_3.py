import cv2
import numpy as np
import matplotlib.pyplot as plt

def translate(img, x, y):
   
    M = np.float32([[1, 0, x],
                     [0, 1, y]])
    translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return translated

def rotate(img, theta):
   
    M = cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), theta, 1.0)
    rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return rotated

def scale(img, scale):
   
    M = np.float32([[scale, 0, 0],
                    [0, scale, 0]])
    scaled = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return scaled

def shear(img, x, y):
  
    M = np.float32([[1, x, 0],
                    [y, 1, 0]])
    sheared = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return sheared

def reflect(img, axis):
  
    
    if 'x' in axis.lower():
        reflected = cv2.flip(img, 1)
    if 'y' in axis.lower():
        reflected = cv2.flip(img, 0)
    return reflected

def visualize(img):
    fig = plt.figure()
    plt.imshow(img)
    plt.axis('off')
    return fig

def multiple_image_load():
  
    
    images, img_paths = [], []
    c = int(input('Enter number of files: '))
    for i in range(c):
        img_paths.append(input(f'Enter image path {i + 1}/{c} : '))
    for path in img_paths:
        images.append(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB))
    return images

def images_transform(*images):
   

    transformations = input('Enter transformations to apply to images: ')
    
    for img in images:
        print('Original Image')
        visualize(img)
        if 'translate' in transformations.lower():
            print('Translated Image')
            visualize(translate(img, int(input('Enter x translation: ')), int(input('Enter y translation: '))))
        if 'rotate' in transformations.lower():
            print('Rotated Image')
            visualize(rotate(img, float(input('Enter rotation angle: '))))
        if 'scale' in transformations.lower():
            print('Scaled Image')
            visualize(scale(img, float(input('Enter scale factor: '))))
        if 'shear' in transformations.lower():
            print('Sheared Image')
            visualize(shear(img, float(input('Enter x shear factor: ')), float(input('Enter y shear factor: '))))
        if 'reflect' in transformations.lower():
            print('Reflected Image')
            visualize(reflect(img, input('Enter axis to reflect image along: ')))
            
def main():
   
    imgs = multiple_image_load()
    images_transform(*imgs)

if __name__ == '__main__':
    main()
