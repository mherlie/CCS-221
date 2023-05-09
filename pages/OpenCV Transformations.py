import streamlit as st
from PIL import Image, ImageOps, ImageEnhance

def translation(image):
    # Apply translation transformation to the image
    translated_image = image.transform(
        image.size, Image.AFFINE, (1, 0, 100, 0, 1, 50), resample=Image.BICUBIC
    )
    return translated_image

def rotation(image):
    # Apply rotation transformation to the image
    rotated_image = image.rotate(10, resample=Image.BICUBIC)
    return rotated_image

def scaling(image):
    # Apply scaling transformation to the image
    scaled_image = image.resize((int(image.width * 1.5), int(image.height * 1.8)), resample=Image.BICUBIC)
    return scaled_image

def reflection(image):
    # Apply reflection transformation to the image
    reflected_image = ImageOps.mirror(image)
    return reflected_image

def shear(image):
    # Apply shear transformation to the image
    sheared_image = image.transform(
        image.size, Image.AFFINE, (1, 0.5, 0, 0, 1, 0), resample=Image.BICUBIC
    )
    return sheared_image

def apply_transform(image, transform_fn):
    img_transformed = transform_fn(image)
    return img_transformed

def process_image(file):
    img = Image.open(file)
    img_transformed = apply_transform(img, transform_fn)
    return img_transformed

def main():
    st.title("Image Transformation")

    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    transform_type = st.selectbox("Select Transformation", ["Translation", "Rotation", "Scale", "Reflect", "Shear"])

    transform_fn = None
    if transform_type == "Translation":
        transform_fn = translation
    elif transform_type == "Rotation":
        transform_fn = rotation
    elif transform_type == "Scale":
        transform_fn = scaling
    elif transform_type == "Reflect":
        transform_fn = reflection
    elif transform_type == "Shear":
        transform_fn = shear

    if file is not None and transform_fn is not None:
        img_transformed = process_image(file)
        st.image(img_transformed, caption="Transformed Image", use_column_width=True)
    else:
        st.warning("Please upload an image and select a transformation type.")

if __name__ == "__main__":
    main()
