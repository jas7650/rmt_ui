from enum import Enum

class Mode(Enum):
    CUT = 0
    REVERSE_CUT = 1
    JAM = 2


    def getValues():
        values = []
        for mode in Mode:
            values.append(mode.value)
        return values


    def getModeString(value):
        if value == Mode.CUT.value:
            return "Cut Serve"
        elif value == Mode.REVERSE_CUT.value:
            return "Reverse Cut Serve"
        else:
            return "Jam Serve"
