# Aperture Engineering Kinect2 Camera project

This repository contains Aperture Engineering's UTS MMD Autumn 2018 software.

Depends:
- Ubuntu (we used 16.06)
- ROS Indigo or later (we used Kinetic)
- IAI Kinect2: https://github.com/code-iai/iai_kinect2

## Notes
- Put `source /home/user/catkin_ws/devel/setup.bash` in your bashrc, replacing 'user' with yours.
- Remember to run `catkin_make -DCMAKE_BUILD_TYPE=Release` after any structural changes to the workspace

## Starting an image stream

**1. Kinect2 Bridges**

```
roslaunch kinect2_bridge kinect2_bridge + TAB
```

TAB to pick the correct device serial, make sure the correct kinect camera is connected if trying to run the bridge for that device. You need to run separate bridges for each camera. If you need to add a new camera follow the 'Adding more kinect2 cameras' instructions below.

The bridge prints a line like `[ INFO] [1528197831.998402494]: [Kinect2Bridge::initDevice]   1: <your-chosen-serial-number> (selected)`.

Must run the bridge to start using the kinect2 for anything.

**2. Image stream**

```
rosrun rgb_view_node rgb_view_node.py
```

Saves image data into a bag which can be accessed later. If you have created a package node with different names then you need to run yours.

**3. Change publish speed of any topic**

e.g. To publish SD quality colour images at 20Hz:

```
rosrun topic_tools throttle messages /kinect2/sd/image_color_rect 20 image_throttle
```

do `rostopic list` to see full list of topics. 
If using this, make sure to adjust the 'rgb_view_node.py' (or whatever node which subscribes to these images) to receive messages from this 'image_throttle' node instead of the camera topic directly.

## Adding more kinect2 cameras
Please note that you will need a separate USB 3.0 bus for each added camera.

**1. Find serial number of device**

- Check the barcode on the kinect2 camera for the device serial.

- Add a calibration folder in '/catkin_ws/src/iai_kinect2/kinect2_bridge/data/<serial-number>'.

If not calibrating the camera, copy the calibration files from one of the other folders into it. The calibration won't be as good though.

**2.  Create new bridge launch files for multiple kinects**

- go to '/catkin_ws/src/iai_kinect2/kinect2_bridge/launch' and duplicate one of the current launch files and append the name with the new kinect's serial number e.g. "kinect2_bridge_serial-number.launch"

- Open the file and change the serial-number inside to the new one at:

`<arg name="base_name"         default="kinect2_serial-number"/>`
and 
`<arg name="sensor"            default=serial-number/>`

- You may now run the new bridge using the instructions in 'starting an image stream'

## Adding a new node package

1. You can add a new node to the catkin_ws package by following the ros website instructions on creating a package. 
2. Add a folder called 'scripts' in the package folder and save the publisher or subscriber code you create for running the node in it. An example of simple subscriber that (saves image data from a topic in a rosbag) is our rgb_view_node.py in **rgb_view_node/scripts**.
3. Navigate to **src/iai_kinect2/iai_kinect2** and open package.xml in gedit. Add the run depend for the new package like `<run_depend>Name_of_package</run_depend>` and save.
4. Run `catkin make` to build the new workspace.


