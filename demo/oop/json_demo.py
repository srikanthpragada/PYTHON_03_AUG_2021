import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


t = Time(10, 20, 30)
s = json.dumps(t.__dict__)  # JSON Serialization
print(s)
d = json.loads(s)  # JSON Deserialization
print(d)
