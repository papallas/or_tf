#!/usr/bin/env python
import IPython
from openravepy import *
from or_tf import OpenRAVE_TF

env = Environment()
env.Load('./testdata/environment.xml')
env.SetViewer('qtcoin')

# Create or_tf instance with frame id.
or_tf_plugin = OpenRAVE_TF(env, "world")

# Get Kinbody from the environment.
object_1 = env.GetKinBody("object_1")

# Register the kinbody to the tf frame that will be used to update its position
# using `rosrun tf tf_monitor` to identify that string.
or_tf_plugin.RegisterBody(object_1, "goal/base_link")

IPython.embed()
