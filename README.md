# <img src = "https://github.com/n3urovirtual/Edge_Detection_Application/blob/main/Images/logo_background.png" width = 400, height = 225>
ETNA (Edge Detection Application) is a Streamlit web application that detects edges in an image, using the multi-stage [Canny Edge Detection algorithm](https://ieeexplore.ieee.org/abstract/document/4767851) (1986).

## Overview
Edge detection is considered to be a vital step in how humans process visual information. To some extent this happens because edges are indicative of object boundaries and shadows, both of which are essential for basic scene understanding (for more read [here](https://www.sciencedirect.com/science/article/pii/S0042698918302050#!)). For many years, edge detection has been used with great success in the field of computer vision. Τhe past few years, though, edge detection, and more specifically edge density, has been  utilized in the field of scene perception as a metric of how cluttered a scene is. Although edge detection, as the name suggests, pertains to the detection of edges in an image, edge density refers to the numbers of pixels in an image that correspond to edges divided by the total number of pixels in that image. In other words, edge density is about how packed with edges an image is. In that sense, an image with high edge density is more likely to be perceived as more cluttered compared to an image with low edge density. As part of my doctoral research, I have been experimenting a lot with edge density and how people search, learn and remember information presented in images with different levels of edge density. For this reason, I decided to make a web application that does exactly that, namely detect edges and calculates edge density. This app can also be used to test UI prototypes. Designs with high edge density are considered visually cluttered and should be redesigned to improve the user experience (UX).

## Description
This is a Streamlit web application that: (a) detects edges in a user-provided image (already implemented), and (b) calculates edge density for that image (to be added soon). To use the app, follow these steps:
1. Upload the image for which you want to detect edges.
2. Specify the lower and upper threshold values (if not specified, default values are taken into account to perform the edge detection).
3. Click on the button "Detect edges".
4. To download the edged image, click on the button "Download image" that appears. 
5. (Edge density calculation step to be added soon).


## How to run the app

To run the app, click [here](https://share.streamlit.io/n3urovirtual/edge_detection_application/main/edge_detection.py).

## Future development

New releases are expected to come out in the next few months. If you would like to add a new feature, feel free to open a pull request or contact me directly. 
