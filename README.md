# Eye Tales

[![HitCount](http://hits.dwyl.io/joelmoff/eye-tales.svg)](http://hits.dwyl.io/joelmoff/eye-tales)
[![GitHub stars](https://img.shields.io/github/stars/joelmoff/eye-tales.svg)](https://GitHub.com/joelmoff/eye-tales/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/joelmoff/eye-tales.svg)](https://GitHub.com/joelmoff/eye-tales/network/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/joelmoff/eye-tales.svg)](https://github.com/joelmoff/eye-tales)
[![GitHub contributors](https://img.shields.io/github/contributors/joelmoff/eye-tales.svg)](https://GitHub.com/joelmoff/eye-tales/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/joelmoff/eye-tales.svg)](https://github.com/joelmoff/eye-tales/blob/master/LICENSE)
[![HitCount](http://hits.dwyl.io/joelmoff/eye-tales.svg)](http://hits.dwyl.io/joelmoff/eye-tales)

[Demo](https://eyetales.asuarez.dev) | [API Documentation](https://api.eyetales.asuarez.dev/ui) | [Devpost](https://devpost.com/software/eyetales)

👁 Tool that helps blind people by describing them their environment

Project built during the sixth edition of Hack The Burgh (2020). It helps blind/visually impared people's life by describing their surroundings using Machine Learning. 

## Inspiration

We wanted to do something that is actually valuable for society so we decided to apply computer science to help blind people's life as much as possible. The idea came when one of the team members saw a blind person in the underground (we are from Barcelona) that hit the recycle bin, he thought about how difficult has to be to walk with a surrounding full of obstacle without seeing. 

## What it does

EyeTales tries to solve this issue by capturing images of the surrounding and describing them with audio to the user. The application captures images from the camera and converts them in base64. Those images are sent to the backend API which generates a text and transforms it to speech. After that, the raw audio is sent back to be reproduced.

The text is generated based on two parts:  the main one is based on the object detection results we get, we take them and we build the sentences based on that; the other one uses a end-to-end system based on deep learning that takes the image and outputs the text.

## How we built it

Frontend and backend are very different components connected by API requests and deployed with [Docker compose](https://docs.docker.com/compose/).

The website was built using Plain JavaScript with the help of jQuery. The backend is done in Python using Flask. The Text2Speech part uses the Google Cloud Speech-To-Text API and the Computer Vision part is build upon two main components: the object detection **Transloadit** API and a [**Show, Attend and Tell**](https://arxiv.org/pdf/1502.03044.pdf) model (neural image captioning model) that was build using Tensorflow 2.0 and trained on a subset of the MS-COCO dataset in Google Colab. 

### Neural Image Captioning Model

Basically the model extracts features using a InceptionV3 from keras applications model zoo with the ImageNet weights (by taking the last layer features), passes them through a CNN encoder and a Recurrent NN decoder that generates the output text.

![](https://kelvinxu.github.io/projects/diags/model_diag.png)

### Backend API

We have the backend which is implemented with [Python 3.7](https://www.python.org/downloads/release/python-370/). For creating the API that allows the communication between the two components, we have used [Flask](https://www.palletsprojects.com/p/flask/) and [OpenAPI](https://swagger.io/specification/) (connected themselves with [Connexion](https://github.com/zalando/connexion) library), integrated with [Docker compose](https://docs.docker.com/compose/). This API is hosted using [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) and [Nginx](https://www.nginx.com/) in a small [Google Cloud](https://cloud.google.com/) engine with 8 CPUs and 32GB of Memory RAM.

## Challenges we ran into

Google Cloud Platform did not deliver us GPU instances so we had to train with Google Colab (which can be painful and stressing some times).
At the beginning I could not get webcam access and when I managed to get access during the conversion to base64 it was converting a white screen.

## Accomplishments that we're proud of

IT WORKS :D!! We get image from the camera, process the image and get an audio that makes sense :D.

Also, despite all the problems we have had, we have been able to train the model and make it work. 

## What we learned

It was the first hackathon for one of the team members, he learnt git and he was in charge of the website but he had no idea, so he had to learn JavaScript, HTML and CSS.
Moreover, we have learned about how Image Captioning based on Deep Learning works (really cool stuff tho) and how to deal with the audio management on JavaScript.

## What's next for EyeTales

We could use another object detection model like MobileNet or TinyYOLO to improve the results outputed and add more rich and real sentences in the script that generates text.  

## Project

### Requirements

1. Python 3.6+
2. Docker CE
3. Docker-compose

### Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

### Usage

To run the server, please execute the following from the root directory:

1. Setup virtual environment

    ```bash
    virtualenv -p /usr/bin/python3.7 env
    source env/bin/activate
    ```

2. Install dependencies

    ```bash
    pip3 install -r requirements.lock
    ```

3. Run Flask server as a python module

    ```bash
    python3 -m src
    ```
    
    as a docker container with docker-compose

    ```bash
    docker-compose up -d --build
    ```

## Authors

- [Adrià Cabeza](https://github.com/adriacabeza)
- [Joel Miarons](https://github.com/joelmoff)
- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © EyeTales
