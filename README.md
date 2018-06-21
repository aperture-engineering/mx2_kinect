#Aperture Engineering Kinect2 Camera project

## Notes
- Put `source /home/user/catkin_ws/devel/setup.bash` in your bashrc, replacing 'user' with urs.
- Remember to run `catkin_make -DCMAKE_BUILD_TYPE=Release` after any structural changes to the workspace

## Starting an image stream

1. **Kinect2 Bridges**

```
roslaunch kinect2_bridge kinect2_bridge + TAB
```

TAB to pick the correct device serial, make sure the correct kinect camera is connected if trying to run the bridge for that device. You need to run separate bridges for each camera. If you need to add a new camera follow the 'Adding more kinect2 cameras' instructions below.

The bridge print a line like `[ INFO] [1528197831.998402494]: [Kinect2Bridge::initDevice]   1: <your-chosen-serial-number> (selected)`.

Must run bridge to start using the kinect2 for anything.

2. **Image stream**

```
rosrun rgb_view_node rgb_view_node.py
```

Saves image data into a bag which can be accessed later.

3. **Change publish speed of any topic:**

e.g. To publish SD quality colour images at 20Hz:

```
rosrun topic_tools throttle messages /kinect2/sd/image_color_rect 20 image_throttle
```

do `rostopic list` to see full list of topics. 
If changing `image_throttle` to something else, make sure to change it in 'rgb_view_node.py'.

## Adding more kinect2 cameras

1. **Find serial number of device**

- Check the barcode on the kinect2 camera for the device serial.

- Add a calibration folder in '/catkin_ws/src/iai_kinect2/kinect2_bridge/data/<serial-number>'.

If not calibrating the camera, copy the calibration files from one of the other folders into it. The calibration won't be as good though.

2.  **Create a new launch file**

- go to '/catkin_ws/src/iai_kinect2/kinect2_bridge/data/<serial-number>' and duplicate one of the current launch files and change the serial number to the serial you want to add.

- Open the file and change the <serial-number> in:

<arg name="base_name"         default="kinect2_<serial-number>"/>
and 
<arg name="sensor"            default="<serial-number>"/>









