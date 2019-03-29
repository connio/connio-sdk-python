# ~~ Read methods ~~
#
# readSerialNumber / cfgSerialNumber
# readLogikaModel / cfgLogikaModel
# readLogikaFwVersion / cfgLogikaFwVersion
# readLevel1Pwd / cfgLevel1Pwd
# readLevel2Pwd / cfgLevel2Pwd
# readLevel3Pwd / cfgLevel3Pwd
# readRelayOutputs / relayOutputs
# readDigitalInputs / digitalInputs
# readMaintCycles / cfgMaintCycles
# readMaintCounters / maintCounters
# readTotalHours / totalHours
# readTotalLoadHours / totalLoadHours
# readLoadPercInLast100h / loadPercInLast100h
# readNbrOfStartsInLastHour / nbrOfStartsInLastHour
# readControllerTime / controllerTime

#
#
#
def readTagIntoProperty_body(pname):
    return """/**

*/
Device.readTagByPropKey(
    { requestKey: '""" + pname + """',
      done: r => done(null, r)
});
"""
def writeChangeAirFilter_body():
    return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "ChangeAirFilter",
  x: value.x || 1,
  setValue: value.setValue,
  byteCount: value.byteCount || 2
};

try {
  let req = Device.makeWriteRequest(args);
  req.done = r => done(null, r);

  Device.writeAndReadTag(req);
}
catch(e) {
  done(e);
}"""

def writeChangeOilFilter_body():
    return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "ChangeOilFilter",
  x: value.x || 1,
  setValue: value.setValue,
  byteCount: value.byteCount || 2
};

try {
  let req = Device.makeWriteRequest(args);
  req.done = r => done(null, r);

  Device.writeAndReadTag(req);
}
catch(e) {
  done(e);
}

  
  """

def writeChangeOil_body():
    return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "ChangeOil",
  x: value.x || 1,
  setValue: value.setValue,
  byteCount: value.byteCount || 2
};

try {
  let req = Device.makeWriteRequest(args);
  req.done = r => done(null, r);

  Device.writeAndReadTag(req);
}
catch(e) {
  done(e);
}

  
  """

def writeChangeSeperatorFilter_body():
    return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "ChangeSeperatorFilter",
  x: value.x || 1,
  setValue: value.setValue,
  byteCount: value.byteCount || 2
};

try {
  let req = Device.makeWriteRequest(args);
  req.done = r => done(null, r);

  Device.writeAndReadTag(req);
}
catch(e) {
  done(e);
}

  
  """

def writeCheckCompressor_body():
    return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "CheckCompressor",
  x: value.x || 1,
  setValue: value.setValue,
  byteCount: value.byteCount || 2
};

try {
  let req = Device.makeWriteRequest(args);
  req.done = r => done(null, r);

  Device.writeAndReadTag(req);
}
catch(e) {
  done(e);
}

  
  """

def writeBearingLubrication_body():
    return """/**
@value {{ x: integer, setValue: integer, byteCount: integer = 2 }}
*/
let args = {
  tagKey: "BearingLubrication",
  x: value.x || 1,
  setValue: value.setValue,
  byteCount: value.byteCount || 2
};

try {
  let req = Device.makeWriteRequest(args);
  req.done = r => done(null, r);

  Device.writeAndReadTag(req);
}
catch(e) {
  done(e);
}"""
