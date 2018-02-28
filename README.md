## Prerequisites
- You need to install the (`openrave_catkin`)[https://github.com/personalrobotics/openrave_catkin] package by just cloning the repository in your `~/catkin_ws/src`.
- Optionally you might also need (`mocap_optitrack`)[https://github.com/ros-drivers/mocap_optitrack] or anything else applicable to your own configuration. `mocap_optitrack` is the
one which publishes the tfs to ROS in our configuration for example, but has nothing to do with `or_tf` plugin.

## Installation
Installation is as simple as cloning this repository in your `~/catkin_ws/src` and then
running `catkin_make` within `~/catkin_ws`.

```bash
cd ~/catkin_ws/src
git clone git@github.com:papallas/or_tf.git
cd ~/catkin_ws
catkin_make
```

You should see a success message at the end of this.

## Let OpenRAVE know about the new plugin
You need to include the following line in your `~/.bashrc` file after you run `catkin_make`:
```bash
export OPENRAVE_PLUGINS=$OPENRAVE_PLUGINS:~/catkin_ws/devel/share/openrave-0.9/plugins
export PYTHONPATH=$PYTHONPATH:~/catkin_ws/src/or_tf/pythonsrc/or_tf
```
Where `openrave-0.9` is the version of your OpenRAVE.

The first line is appending the path where `or_tf` is being built so OpenRAVE is
aware of its path, where the second is letting Python know about the wrapper class
so you can import it into any script and use the wrapper class.

Make sure that you either restart your terminal window or you run `source ~/.bashrc`.

Moreover, verify the success of the installation and configuration by running `openrave --listplugins` and
you should see the following output:
```bash
sensor: ...
.
.
.
or_tf - /.../catkin_ws/devel/share/openrave-0.9/plugins/or_tf_plugin.so
.
.
.
```

## Setting up your script and registering OpenRAVE kinbodies to tf frames
Your code requires the following import:
```python
from or_tf import OpenRAVE_TF
```

And also the following code to initialise the or_tf wrapper class:
```python
# Create or_tf instance with frame id.
or_tf_plugin = OpenRAVE_TF(env, "world")
```

You now need to get our OpenRAVE kinbody:
```python
# Get Kinbody from the environment.
object_1 = env.GetKinBody("object_1")
```

And you need to register the kinbody to the tf plugin:
```python
or_tf_plugin.RegisterBody(object_1, "goal/base_link")
```

How you will find the `goal/base_link` parameter?

Run `rosrun tf tf_monitor` and you should get a similar output to this one:
```bash
RESULTS: for all Frames

Frames:
Frame: base published by unknown_publisher Average Delay: 7.94464 Max Delay: 7.96316
Frame: base_link published by unknown_publisher Average Delay: 7.94463 Max Delay: 7.96316
Frame: ee_link published by unknown_publisher Average Delay: 7.94463 Max Delay: 7.96316
Frame: forearm_link published by unknown_publisher Average Delay: 8.44579 Max Delay: 8.45808
Frame: goal/base_link published by unknown_publisher Average Delay: 2.97504 Max Delay: 2.9932
Frame: robot/base_link published by unknown_publisher Average Delay: 2.97725 Max Delay: 3.00143
Frame: shoulder_link published by unknown_publisher Average Delay: 8.4458 Max Delay: 8.45808
Frame: tool0 published by unknown_publisher Average Delay: 7.94463 Max Delay: 7.96316
Frame: tool0_controller published by unknown_publisher Average Delay: 8.44492 Max Delay: 8.45965
Frame: upper_arm_link published by unknown_publisher Average Delay: 8.4458 Max Delay: 8.45808
Frame: wrist_1_link published by unknown_publisher Average Delay: 8.4458 Max Delay: 8.45808
Frame: wrist_2_link published by unknown_publisher Average Delay: 8.4458 Max Delay: 8.45808
Frame: wrist_3_link published by unknown_publisher Average Delay: 8.4458 Max Delay: 8.45808
```

From there you can see the `goal/base_link` which is the one you need. The name `goal`
is coming from your configuration and is subject to your setup. For example if you are
using OptiTrack and you are using the ROS Package (`mocap_optitrack`)[http://wiki.ros.org/mocap_optitrack]
then the `goal` will be whatever you have named your frame in the `config/mocap.yaml` file:
```yaml
#
# Definition of all trackable objects
# Identifier corresponds to Trackable ID set in Tracking Tools
#
rigid_bodies:
    '1':
        pose: goal/pose
        pose2d: goal/ground_pose
        child_frame_id: goal/base_link
        parent_frame_id: world
optitrack_config:
        multicast_address: 224.0.0.1
```

where `1` is the `user_id` in OptiTrack.

A `testplugin.py` file is provided as an example.

## Contributors
or_tf plugin was developed by the Robotics Lab in the School of Computing at
the University of Leeds. This software is initially developed by Mehmet Dogar
and is currently maintained by [Rafael Papallas](https://github.com/papallas).
