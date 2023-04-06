# Setup

# ROS Tutorial

``` cmd
cd ~/catkin_ws/src
catkin_create_pkg ros_test std_msgs rospy

cd ros_test
vim package.xml

catkin build ros_test

roscd ros_test
mkdir scripts
cd scripts
vim talker.py listener.py -p

catkin build ros_test

source ~/catkin_ws/devel/setup.bash

roscore &

rosrun ros_test talker.py
rosrun ros_test listener.py
```



