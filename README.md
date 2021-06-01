# ros-averager

This package contains a ros node *(averager)* that can calculate the average over the last *n* samples recieved from a subscribed topic (*~raw*). It then publishes the average to a topic (*~avg*). *n* is defined and set in the ros parameter space as 'buffer_size'.

Two other nodes *(square_generator* and *triangle_generator)* generate and publish (to the topic *~raw*) a square wave signal and a triangle wave signal.

Using a launch file, two instances of the averager is produced. One subscribes to an instance of the *square_generator*, and the other to an instance of the *triangle_generator* and the average of each function is calculated and published to seperate topics defined using topic remapping from the launch file.

Parameters (such as amplitude, frequency etc.) of the square and triangle functions are defined in YAML files in the **config** folder, which are used by the launch file when instantiating the nodes.

