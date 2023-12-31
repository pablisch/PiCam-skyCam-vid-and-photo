# PiCam skyCam video & photo capture

This is a relatively simple python script to alternate between short videos and still photos with the Raspberry Pi camera module.
It was written to capture videos and images during a high altitiude balloon flight where the payload was fitted with cameras facing upwards, outwards and downwards to captue the different views during the flight.

The video duration can be changed by editing the `sleep(x)` in the code on line 16.

The number of pictures taken can be changed by editing the second paramater of the `for` loop in the code.

The file can be set to automatically run on boot by adding the following line to the `/etc/rc.local` file:

`sudo python /home/pi/picam_simple.py &`

The `&` is important as it allows the script to run in the background.

The script can be stopped by running the following command:

`sudo killall python`

A Raspberry Pi with camera module:
![Raspberry Pi with camera module](images/camera-module.png)

Photos taken during the high altitude balloon flight:
![The moment the balloon burst](images/balloon-burst.png)

![The launch site below](images/launch-site.jpg)

![Half way up](images/half-way-up.jpg)

You can also see a video of the moment the balloon burst [here](https://drive.google.com/file/d/1lMgBaVS7oJdVSEwQzxkLll81O-rPzlPR/view?usp=sharing).

