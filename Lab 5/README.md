# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

#### Contours:
![image](https://user-images.githubusercontent.com/29494260/140816273-4d110210-9ab7-4391-beaa-3ad2e93b36e3.png)

### The contours algorithm could be used to to create a stencil tracing device. The device would take an image and return the contours of the objects in the image so that an artist can trace over the lines. For example, an artist who is trying create a still life painting can use this as a way to get the proprotions of their painting correct before filling in details. See below an image of a street artist using stencils to create their art. 
![image](https://user-images.githubusercontent.com/29494260/140821574-eee79118-ffd3-4660-b0b0-67448797521e.png)



#### Face Detection:
![image](https://user-images.githubusercontent.com/29494260/140816132-55545ccf-ed0a-46a0-afb4-8d61ff4ecdbc.png)

### The face detection algorithm can be used to create a device that dispenses candy whenever a person shows their face to it. As long as the device sees two eyes and a mouth, it would release the candy by activating a servo motor to open the candy gate. 

#### Flow Detection:
![image](https://user-images.githubusercontent.com/29494260/140816734-f41c63ff-61d3-4145-a2d3-4d616877dc9a.png)
### The flow dection algorithm can be used to create a Red-Light Green-Light children's game. Red-Light Green-Light is a game where a moderator says "red light" when players are supposed to be still and "green light" when players are supposed to move forward. The device would sit beside the flow of the players and use flow detection to determine when a player is moving during a red light. The device could speak in order to indicate who was identified as "out" in the game.  

![image](https://user-images.githubusercontent.com/29494260/140822847-fd0cea7d-d69f-4a95-9479-e353ea1cfae6.png)


#### Object Detection:
![image](https://user-images.githubusercontent.com/29494260/140817160-b94cbd71-ee4c-41d2-9c95-65dc95831611.png)

### The object detection algorithm could be used to create a device that detects how messy your room is. Every object that is detected by the device would be considered clutter and it would display a messiness score depending on how much clutter is in your room. When the amount of clutter is above a threshold, it would flash a red light to indicate that it is time to clean up. 

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

![image](https://user-images.githubusercontent.com/29494260/140826888-a369a476-7e54-43b2-ba38-83ffb9227746.png)

### Invisible Keyboard: Media pipe could be used to track the location of fingers while a user types. As the user types more, the device would use the data generated by media pipe to learn how the user's hand looks while they type. After lots of data has been colleted, the device would be able to infer what the user is typing without input from the keyboard. The physical keyboard could then be removed entirely to allow the user to type without a physical keyboard. 
![image](https://user-images.githubusercontent.com/29494260/140828312-a59dc4d3-7f91-4e10-a985-51758396be0c.png)


(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***
![image](https://user-images.githubusercontent.com/29494260/140830157-a2d1550a-6e33-44ce-972c-d628807a521b.png)

### The classifier could be used to create a device that alerts a driver when they are falling asleep at the wheel. The device would sit on the user's dashboard with the lens pointed at the user while they drive. When the model recognizes the symptoms of a sleepiness in the driver's face it alerts them to pull over and rest. 


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

I used the media pipe algorithm to create an American Sign Language interperator. The device can detect static sign language symbols such as the ones below.

![image](https://user-images.githubusercontent.com/29494260/140843010-fd5ae3eb-22dd-4faa-bf9d-bab8850c36aa.png)

The goal of this interaction is to replace typing at a keyboard with sign language. Typing at a keyboard for prolonged periods of time is unhealthy. Using sign language to interact with the computer is more active and might be a healthier alternative because it keeps the arms more engaged. 

Experimentation: 
1. I selected several easy to recognize signs from the table above: "yes", "money", "I love you", "I am", and "fine". 
2. I implemented the signs by hard coding thresholds for distances between fingers for each sign.
3. I held up each sign to test if the system could recognize them. 

#### See all code in sign_language.py

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
- It mostly works as intended. When the user places their hand 6 to 12 inches from the camera and holds it there briefly, the protoype is accurately able to detect the sign.
2. When does it fail?
- It fails when the hand is too far away from the camera or too close to the camera. It also identifies signs while in between gestures which can get confusing. 
3. When it fails, why does it fail?
- This failure occurs because I have set manual thresholds for the distances between fingers in order to detect signs. A more robust method would detect the ratios of the distances between the fingers. 
4. Based on the behavior you have seen, what other scenarios could cause problems?
- It is possible for the device to fail when the hand sign is not perfectly aligned with the camera. For example, if the hand is slightly tilted, the distances between fingers change (using proportions as suggested in 4 would not correct this issue). It is also possible for symbols that look similar to be misclassifid more often than symbols that look very different. 

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
- Since they will receive realtime feedback from the system, they will immediately realize when it fails and therefore immediately become aware of its uncertainties.

1. How bad would they be impacted by a miss classification?
- If the misclasification happens frequently, then then the user will have a bad experience using their computer. This is akin to having an unreliable keyboard. They might be able tolerate it for some time, but they will eventually get irritated enough to replace it. 

1. How could change your interactive system to address this?
- Instead of using american sign language, I could create a different set of symbols that are easier for the device to classify. The dowside of this approach is that everyone would need to learn an entirely new set of symbols, and it would be like learning how to type all over again. 

1. Are there optimizations you can try to do on your sense-making algorithm.
- Using proportions instead of absolute distances between fingers would make the algorithm more robust to changes in distance. 
- I could use a more sophisticated model to identify gestures that are strung together to make sentences instead of just individual words. 
### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
It can be used to interact with a computer without a keyboard. Ideally, typing through sign language provides a healthier alternative to traditional physical keyboards. 
* What is a good environment for X?
The device must be used in a well-lit environment with a stationary background and only one user within its field of view.  
* What is a bad environment for X?
Using the device in a scene where there are hands from multiple people will not work. Obstructing the device's vision will prevent it from being able to see the hand signs so the field of view must be clear. 
* When will X break?
The device breaks when the user places their hand too close or too far from the camera. It also breaks when the hand is not fully in the field of view of the camera. 
* When it breaks how will X break?
It breaks by not displaying the proper words for the sign or not displaying any words at all.  

* How does X feel?
Every time the device correctly classifies a sign, I feel excited in the same way that I would feel if I were winning points in a videogame. Also, when I see the mesh drawn on my hand it makes me feel like there is actually something physically on my hand. 

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***
Please click image below to see video: 
[![Alt text](https://user-images.githubusercontent.com/29494260/140859631-2e4e7c6c-77af-44b6-9482-0c34d989f954.png)](https://drive.google.com/file/d/1A3mctZ372rYyT6Si9TarfjuZi3PCtJnW/view?usp=sharing)
### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
