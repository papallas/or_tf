#!/usr/bin/env python
from openravepy import *
import IPython
from or_tf import OpenRAVE_TF

RaveInitialize()
RaveLoadPlugin('lib/or_tf')
env = Environment()
env.Load('./testdata/environment.xml')
env.SetViewer('qtcoin')

or_tf_plugin = OpenRAVE_TF(env, "world")
object_1 = env.GetKinBody("object_1")
or_tf_plugin.RegisterBody(object_1, "goal/base_link")

IPython.embed()
