# ROS Drone Basic Course for Beginners
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Course-Workflow">Course Workflow</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Pre-Course-Requirments">Pre-Course Requirments</a></li>
    <li><a href="#Notes">Notes</a></li>
    <li><a href="#License">License</a></li>
  </ol>
</details>

## About this Repository
Hector Drone and  its sensors is what we are going to interface our python Nodes with and write algorithms to avoid obstacles and secure diamonds in simulation of Gaebzo .OpenCV library for python is going to be used for the Last project and you will learn how to perform computer vision algorithms with ROS .

- ![alt text](https://github.com/noshluk2/ROS2-Drone-Basic-Course-for-Beginners/blob/master/Images/thumbnail.png)
- **[[Get course Access]](https://robotisim.com/project-based-course/)**
----
## Using this Repository
* Move into your workspace/src folder
  ```
  cd path/to/ros2_ws/src/
  ##e.g cd ~/ros2_ws/src/
    ```
* Clone the repository in your workspace
  ```
  git clone --recurse-submodules https://github.com/noshluk2/ROS2-Drone-Basic-Course-for-Beginners
  ```
* Perform make and build through colcon
  ```
  cd /path/to/workspace_root/
  ##e.g ~/ros2_ws/
  colcon build
  ```

* Source your Workspace in any terminal you open to Run files from this workspace
  ```
  source /path/to/ros2_ws/devel/setup.bash
  ```
- launch go to goal behaviour
  ```
  ros2 launch  drive_drone p2_go_to_goal.launch.py
  ```
----
## Course Workflow
This course is going to utilize Hector drone package containing a drone with multiple sensors. We will start with creating custom launch files which will bring all required files into our custom package. Sensors integration to robot model with xacro files .We will then perform multiple tasks to learn how ROS can help in learning drone robotics

Custom World Files will be created to represent projects , and complete workflow of our projects will be explained .

OpenCV library for python is going to be used for the Last project and you will learn how to perform computer vision algorithms with ROS


---
## Features
* **Drone Following Ground Vehicles throuhg Computer Vision**
  -  ![alt text](https://github.com/noshluk2/ROS2-Drone-Basic-Course-for-Beginners/blob/master/Images/drone_follow_tb3.gif)
* **Drone performing dynamic Go to Goal behaviour**
  -  ![alt text](https://github.com/noshluk2/ROS2-Drone-Basic-Course-for-Beginners/blob/master/Images/drone_gtg.gif)


----
## Pre-Course Requirments

**Software Based**
* Ubuntu 22.04 (LTS)
* ROS2 - Humble

----
## Notes

- We have uploaded all the notes made during the lectures of the course so you can get more out of this repository with the instructors Notes. A seperate folder named as **Notes** contain a single PDF carrying all the notes in the root of this repository
----

## License

Distributed under the GNU-GPL License. See `LICENSE` for more information.
