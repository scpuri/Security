#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            �J��s�,�&z�+��͎�x"j�E�:�Kң鐻��� �k
�\�M��r289��Z8�:i�G<�8��q#T�Zxk�8W���|���˫Ν�:<ˍ��b�)��޼�l�}�s���G���_
"""
from hashlib import sha256
if(sha256(blob).hexdigest()[0] > sha256(blob).hexdigest()[1]):
	print "I come in peace."
else:
	print "Prepare to be destroyed!"

