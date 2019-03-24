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
