# ChangeBackgroundToAImage
MediaPipe Selfie Segmentation !

## Requirements
  * Python 3.9
  * requirements.txt

## Change background
This is an application of selfie segmentation using MediaPipe to change the background.
This process is implemented python, and the following libraries:
  * OpenCV (For testing)
  * Numpy (Matrix application)
  * MediaPipe (For mask)

## MediaPipe
MediaPipe offers ML solutions for live and streaming medio. The selfie segmentation segments the prominent humans in the scene. This provide 2 model based on MobileNetV3, a general model and a landscape model.
For more information visit the [page](https://google.github.io/mediapipe/solutions/selfie_segmentation).

The input image is:

![Input image][lil-input-url]

The result obteined just changing the background with a color

![Output][lil-output-url]

Now, the background is other photo.

![Background 1][lil-bg-url]

The result is:

![Output background 1][lil-outputbg1-url]

The last test with other photo.

![Background 2][lil-bg2-url]

The result is:

![Output background 2][lil-outputbg2-url]


[lil-input-url]: https://raw.githubusercontent.com/oguapi/ChangeBackgroundImage/master/data/photo.jpg
[lil-bg-url]: https://raw.githubusercontent.com/oguapi/ChangeBackgroundImage/master/data/background.jfif
[lil-bg2-url]: https://raw.githubusercontent.com/oguapi/ChangeBackgroundImage/master/data/background2.jfif
[lil-output-url]: https://raw.githubusercontent.com/oguapi/ChangeBackgroundImage/master/output.jpg
[lil-outputbg1-url]: https://raw.githubusercontent.com/oguapi/ChangeBackgroundImage/master/outputBg.jpg
[lil-outputbg2-url]: https://raw.githubusercontent.com/oguapi/ChangeBackgroundImage/master/outputBg2.jpg