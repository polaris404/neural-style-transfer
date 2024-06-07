import streamlit as st
from pathlib import Path
from neural_style_transfer import generate_img

def display_img(org_img, style_img):
    img = generate_img(org_img, style_img)
    st.image(img, caption='Result after Neural Style Transfer', use_column_width=True)

def main():
    content_img = "./sample/konark.jpg"
    result_img = "./sample/result.jpg"
    markdown=f'''
    # Neural Style Transfer

## Introduction

As the title suggests, Neural Style Transfer is a technique in deep learning in which style of one image is applied to the content of another image. The application takes two input images, a content image and a style image. The output is a new image that maintains the content of the content image but has the artistic style of the style image.

I've used `arbitrary-image-stylization-v1` model trained on Tensorflow available on [kaggle](https://www.kaggle.com/models/google/arbitrary-image-stylization-v1/tensorFlow1/256/2). It takes two input images of size 245X256 and outputs the image of the same size.

Here is an example of it:

<div>
	<div style="display: flex;justify-content: center;">
		<div style="text-align: center;margin: 10px;">
			<img style="display: block; margin: 0 auto;height: 256px;" src="{content_img}">
			<p style="margin-top: 5px;font-style: italic;color: #888;">Photo of Konark Temple captured by me.</p>
		</div>
		<div style="text-align: center;margin: 10px;">
			<img style="display: block; margin: 0 auto;height: 256px;" src="./sample/femme_nue_assise.jpg">
			<p style="margin-top: 5px;font-style: italic;color: #888;">Femme Nue Assise by Picasso</p>
		</div>
	</div>
	<div style="text-align: center;margin: 10px;">
		<img style="display: block; margin: 0 auto;height: 256px;" src={result_img}>
		<p style="margin-top: 5px;font-style: italic;color: #888;">Resulant Image</p>
	</div>
</div>

## How it works?

### Visualizing ConvNet

To understand style transfer you should first know what each layer in a Convolution Neural Network learns. Here is paper published on visualizing CNN: [Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901).

- They proposed a technique which uses multi-layered Deconvolution Network (deconvnet), to project the feature activations back to the input pixel space. A deconvnet can be thought of as a convnet model that uses the same components (filtering, pooling) but in reverse, so instead of mapping pixels to features does the opposite.
- To examine a convnet, a deconvnet is attached to each of its layers, providing a continuous path back to image pixels. To examine a given convet activation, they set all the other activations in the layer to zero and pass it to the attached deconvnet layer.
- After training, we can visulalize what feature does the particular layer is learning.

### Neural Style Transfer

A paper was published on 2015 named [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576). In this paper the researchers found that the representations of content and style in the CNN are separable. That is, we can manipulate both representations independently to produce new, perceptually meaningful images.

- Higher layers in the network capture the high-level content in terms of objects and their arrangement in the input image but do not constrain the exact pixel values of the reconstruction. In contrast, reconstructions from the lower layers simply reproduce the exact pixel values of the original image.
- We therefore refer to the feature responses in higher layers of the network as the **content representation** and in lower layers as **style representation**.

    '''
    # with open('README.md', 'r') as f:
    #     markdown = f.read()
    st.markdown(markdown, unsafe_allow_html=True)    
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header('Original Image')
            org_img = st.file_uploader(label='Upload original image', type=['png', 'jpg', 'jpeg'])
        with col2:
            st.header('Style Image')
            style_img = st.file_uploader(label='Upload style image', type=['png', 'jpg', 'jpeg'])

        if org_img is not None and style_img is not None:
            if st.button("Submit"):
                col1, col2, col3 = st.columns([1,2.5,1])
                with col2:
                    display_img(org_img.read(), style_img.read())


if __name__ == '__main__':
    main()