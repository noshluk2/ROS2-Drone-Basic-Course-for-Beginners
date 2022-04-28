# ROS Drone Basic Course for Beginners
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Course-Workflow">Course Workflow</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Link-to-the-Course">Link to the Course</a></li>
    <li><a href="#Notes">Notes</a></li>
    <li><a href="#Instructors">Instructors</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About this Repository
Hector Drone and  its sensors is what we are going to interface our python Nodes with and write algorithms to avoid obstacles and secure diamonds in simulation of Gaebzo .OpenCV library for python is going to be used for the Last project and you will learn how to perform computer vision algorithms with ROS .

- ![alt text](https://github.com/noshluk2/ROS-Drone-Basic-Course-for-Beginners/blob/master/Images/drone.png)
- **[[Get course Here]](https://www.udemy.com/course/robotics-with-ros-autonomous-drone-with-path-planning-slam/?couponCode=APRIL_END)**
----
## Using this Repository
* Ubuntu 20.04 and ROS1-Noetic should be installed 
* Move into your workspace/src folder
 ```
 cd path/to/ros1_ws/src/
##e.g cd ~/catkin_ws/src/
  ```
* Clone the repository in your workspace
```
git clone https://github.com/noshluk2/ROS-Drone-Basic-Course-for-Beginners
```
```
git clone https://github.com/RAFALAMAO/hector_quadrotor_noetic
```


* Perform make and build through catkin
 ```
 cd /path/to/workspace_root/
 ##e.g ~/catkin_ws/
 catkin_make
 ```
 
* Source your Workspace in any terminal you open to Run files from this workspace ( which is a basic thing of ROS )
```
source /path/to/catkin_ws/devel/setup.bash
```
- (Optional for Power USERs only) Add source to this workspace into bash file
 ```
echo "source /path/to/catkin_ws/devel/setup.bash" >> ~/.bashrc
 ```
  **NOTE:** This upper command is going to add the source file path into your ~/.bashrc file ( Only perform it once and you know what you are doing).This will save your time when running things from the Workspace

----
## Course Workflow
This course is going to utilize Hector drone package containing a drone with multiple sensors. We will start with creating custom launch files which will bring all required files into our custom package. Sensors integration to robot model with xacro files .We will then perform multiple tasks to learn how ROS can help in learning drone robotics

Custom World Files will be created to represent projects , and complete workflow of our projects will be explained .

OpenCV library for python is going to be used for the Last project and you will learn how to perform computer vision algorithms with ROS 


---
## Features
* **Flying through Sensor data manipulation** 
  -  ![alt text](https://github.com/noshluk2/ROS-Drone-Basic-Course-for-Beginners/blob/master/Images/hector_drone.gif)
* **Making Obstacle Avoiding Drone** 
  -  ![alt text](https://github.com/noshluk2/ROS-Drone-Basic-Course-for-Beginners/blob/master/Images/obstacle_avoiding.gif)
* **Diamond Securing Drone Surveillance** 
  -  ![alt text](https://github.com/noshluk2/ROS-Drone-Basic-Course-for-Beginners/blob/master/Images/diamond_secure.gif)
* 


----
## Pre-Course Requirments 

**Software Based**
* Ubuntu 20.04 (LTS)
* ROS1 - Noetic
---
## Link to the Course

- **[[Get Discounted Coupon Here]](https://www.udemy.com/course/robotics-with-ros-autonomous-drone-with-path-planning-slam/?couponCode=APRIL_END)**

----
## Notes

- We have uploaded all the notes made during the lectures of the course so you can get more out of this repository with the instructors Notes. A seperate folder named as **Notes** contain a single PDF carrying all the notes in the root of this repository
----

## Instructors

Muhammad Luqman (ROS Simulation and Control Systems) - [Profile Link](https://www.linkedin.com/in/muhammad-luqman-9b227a11b/)  

----
## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.
