#!/usr/bin/python
import datetime,json

sampledict = {}
sampledict['a'] = "some string"
sampledict['b'] = datetime.datetime.now()

print sampledict   # output : {'a': 'some string', 'b': datetime.datetime(2017, 4, 15, 5, 15, 34, 652996)}

#print json.dumps(sampledict)

'''
output : 

Traceback (most recent call last):
  File "./jsonencodedecode.py", line 10, in <module>
    print json.dumps(sampledict)
  File "/usr/lib/python2.7/json/__init__.py", line 244, in dumps
    return _default_encoder.encode(obj)
  File "/usr/lib/python2.7/json/encoder.py", line 207, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python2.7/json/encoder.py", line 270, in iterencode
    return _iterencode(o, 0)
  File "/usr/lib/python2.7/json/encoder.py", line 184, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: datetime.datetime(2017, 4, 15, 5, 16, 17, 435706) is not JSON serializable


'''

sampledict['b'] = datetime.datetime.now().strftime("%B %d, %Y %H:%M %p")

afterdump = json.dumps(sampledict)

print afterdump  #output : {"a": "some string", "b": "April 15, 2017 05:18 AM"}

print type(afterdump) #<type 'str'>


afterloads = json.loads(afterdump) 

print afterloads # output : {u'a': u'some string', u'b': u'April 15, 2017 05:18 AM'}


print type(afterloads) # output :<type 'dict'> 



