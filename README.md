# final-project
Autonomous Car  
A battery powered car. The car will be able to follow lane/road with marking. It will use camera to find the path angle and run over the path.

Here are the links of the tutorial that I have followed to build my self driving car. 
I did not made exact replica, I have changed some things to simplify the project.

Playlist: 
Title: Self Driving Car with Lane Detection using Raspberry Pi (2020)
https://www.youtube.com/playlist?list=PLMoSUbG1Q_r_wT0Ac7rOlhlwq9VsZDA0b

First part of the 6 part youtube tutorial of murtaza's Self Driving Car:
Title: Self Driving Car with Lane Detection using Raspberry Pi | OpenCV (2020) p.1
https://youtu.be/aXqoPiMPhDw

Free full course:
https://www.murtazahassan.com/courses/self-driving-car-using-raspberry-pi/

https://www.murtazahassan.com/courses/raspberry-pi-ultimate-robot/
            https://www.murtazahassan.com/courses/self-driving-car-using-raspberry-pi/
            https://github.com/murtazahassan/Raspberry-Pi-Ultimate-Robot
            https://www.youtube.com/playlist?list=PLMoSUbG1Q_r_wT0Ac7rOlhlwq9VsZDA0b
                


## Hardware: 

Parts list: [N.B.: Unit prices are approximate]  
    
    - Raspberry Pi 3B+ (1pc)-------------------------  (4500tk)
    - MicroSD card 16GB (1pc)------------------------   (500tk)  
    - Pi camera (1pc)--------------------------------  (2000tk)  
    
    - 90 degree angled small plastic gear motor (2pc)    (60tk)
    - Wheel Caster (1pc)----------------------------     (90tk)
    - Plastic wheel (2pc)---------------------------     (60tk)  
    
    - L293d Motor Driver IC (1pc)-------------------     (40tk)
    - Double battery holder for 18650 (2pc)---------     (40tk)
    - Mini breadboard (1pc)-------------------------     (60tk)
        

## Software:
Without machine Learning there are two methods for lane detection:  
- Histogram method  
- Canny-Hough Line detection
    
murtaza's histogram method is tested with modification.

## Other-options directory

### Histogram 
- histogram simple    
The very first one uses simple code. But it has no details or description. Also uses python2. So can not be used by a beginner.  
Requires more expertise to debug it.
- histogram lane pi murtaza    
This is the main directory where I worked, followed tutorial and developed my own working version of self driving car

### Canny Hough 
collected from : https://www.hackster.io/Abhinav_Abhi/road-lane-detection-with-raspberry-pi-a4711f    
Did not try myself.
    

