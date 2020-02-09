class ArmJointState:
    def __init__(self, state):
        self.state = state
        self.position1, self.position2, self.position3, self.position4, self.position5, self.position6 = state

    def __repr__(self):
        return "<ArmJointState(%s)>" % self.state
