#!/usr/bin/env python

"""Convert index into the ILSVRC2012 Imagenet 1000 classes to its class name."""

import json

classes = json.load(open("imagenet1000.json"))

class_index = 587  # An example index. One of the 1000 classes.
class_name = classes[class_index]  # This should be "hammer"

print("Class index: {}, Class name: {}".format(class_index, class_name))
