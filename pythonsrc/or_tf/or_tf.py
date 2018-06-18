#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

import openravepy as orpy
import IPython

class OpenRAVE_TF:

    def __init__(self, env, world_tf_id):
        self.env = env
        self.world_tf_id = world_tf_id

        self.or_tf = orpy.RaveCreateSensor(self.env,'or_tf or_tf '+self.world_tf_id)
        env.Add(self.or_tf)

    def RegisterBody(self, or_body, tf_id, openrave_frame_in_tf_frame=None, planar_tracking=False, fixed_translation_z=-1.0):
        x = 0.0
        y = 0.0
        z = 0.0
        qw = 1.0
        qx = 0.0
        qy = 0.0
        qz = 0.0

        if openrave_frame_in_tf_frame is not None:
            x = openrave_frame_in_tf_frame[0,3]
            y = openrave_frame_in_tf_frame[1,3]
            z = openrave_frame_in_tf_frame[2,3]
            quat = orpy.quatFromRotationMatrix(openrave_frame_in_tf_frame[:3,:3])
            qw = quat[0]
            qx = quat[1]
            qy = quat[2]
            qz = quat[3]

        cmd = 'RegisterBody ' + or_body.GetName() + ' ' + tf_id + ' openrave_frame_in_tf_frame ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(qw) + ' ' + str(qx) + ' ' + str(qy) + ' ' + str(qz)

        if planar_tracking:
            cmd +=' planar_tracking' + ' ' + 'fixed_translation_z' + ' ' + str(fixed_translation_z)

        self.or_tf.SendCommand(cmd)

    def RegisterRobotHand(self, or_body, tf_id):
        self.or_tf.SendCommand('RegisterRobotHand ' + or_body.GetName() + ' ' + tf_id)

    def UnregisterBody(self, or_body):
        self.or_tf.SendCommand('UnregisterBody ' + or_body.GetName())

    def Pause(self):
        self.or_tf.SendCommand('Pause')

    def Resume(self):
        self.or_tf.SendCommand('Resume')

    def Clear(self):
        self.or_tf.SendCommand('Clear')
