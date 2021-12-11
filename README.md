# vnuk-ai-challenge1
Repository for challenge 1 of Artificial Intelligence course

>

<
[![Contributors][contributors-shield]][https://github.com/shayongithub]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/shaynguyen-ds/]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
    <img src="https://cdn.vox-cdn.com/thumbor/48ZYdXopLsPslD4J6lZCruEQJIw=/0x0:1185x747/1200x0/filters:focal(0x0:1185x747):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/7475709/Screen_Shot_2016_11_15_at_12.05.46_PM.png" alt="Logo" width="100%" height="100%">
  </a>

  <h2 align="center">Convolutional Neural Network with QuickDraw Doodle Dataset</h2>


</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)



* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

We create an app which gives an EMOJI, then identifies the face expression of the users and finally compare if the face expression is similar with the emoji . 

Here's why:
*Highly entertaining, players can practice facial muscles.
*High interaction between the game and the player.
*Apply in practice the learned knowledge (image recognition).
*Try to solve challenges.
Function :
cv2.CascadeClassifier('.xml') 
>>> identify the face 

dlib.get_frontal_face_detector() 
dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
>>> identify the landmark

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Flask](https://flask.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

This package assumes using Python 3.x

### Prerequisites

Before you continue, ensure you have met the following requirements:

* You have already install Visuall Studio C++
* You have installed the latest version of OpenCV, Cmake, Dlib and Numpy(Numpy and OpenCV have to share the same version).
* Linux, Mac OS or Windows are all currently supported.

The easiest way to install it is using either pip or conda:

| **Using pip**                | **Using conda**                            |
|------------------------------|--------------------------------------------|
| `pip install ...` | `conda install -c ...` |
|                              |                                            |

```sh
pip install opencv-python
```
```sh
pip install cmake
```
```sh
pip install dlib
```

### Installation

####Get the face Comparision With Emoji source code
```sh
git clone https://github.com/hauchieu/PythonProject.git
```


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

This is the screen when you select to record video (you can enter Y for Yes or N for No).
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/master/usagee/record.png" width="400" height="200">
</p>

All the pictures below are screenshots when playing a game, players will create facial expressions similar to stickers displayed on the game frame.
Surprise face sticker with mouth wide and eyes closed.
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/master/usagee/surprise.png" width="400" height="200">
</p>

Smiley face sticker
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/master/usagee/smile.png" width="400" height="200">
</p>

Sad face sticker
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/5683e182fb405a82fa61160d09f4bf755c6fb78f/usagee/sad.png" width="400" height="200">
</p>

Neutral face sticker
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/5683e182fb405a82fa61160d09f4bf755c6fb78f/usagee/neutral.png" width="400" height="200">
</p>

Blink face sticker
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/master/usagee/blink.png" width="400" height="200">
</p>

This is the video slideshow screen recorded.
<p align="center">
  <img src="https://github.com/hauchieu/PythonProject/blob/5683e182fb405a82fa61160d09f4bf755c6fb78f/usagee/show.png" width="400" height="200">
</p>

<!-- CONTACT -->
## Contact

For more info, contact Đạt (Leader) - email: dat.nguyen190401@vnuk.edu.vn

Project Link: [https://github.com/hauchieu/PythonProject]

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Drowsiness detection with OpenCV](https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/)
* [Face landmarks detection](https://youtu.be/MrRGVOhARYY)
* [How to Record Video in OpenCV](https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python)
* [How to show videos frame by frame](https://stackoverflow.com/questions/54307228/how-to-show-videos-frame-by-frame-with-key-presses-with-python-cv2)
* [How To Use Break, Continue, and Pass Statements](https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
