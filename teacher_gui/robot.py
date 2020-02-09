from moveo_moveit import msg
import rospy

ArmJointState = msg.ArmJointState


class Robot:
    def __init__(self, name, initial_state=(0, 0, 0, 0, 0, 0)):
        self.initial_state = list(initial_state)
        self.name = name
        self._current_state = None
        input('Press Enter to move to initial position: ' + str(initial_state))
        self.move_to_start_position()

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, state):
        self.update_state(state)

    def move_to_start_position(self):
        self.current_state = self.initial_state

    def set_joint(self, index, value):
        new_state = self.current_state
        new_state[index] = value
        self.current_state = new_state

    def update_state(self, state):
        pub = rospy.Publisher('joint_steps', ArmJointState, queue_size=4)
        rospy.init_node('teacher', anonymous=True)

        rate = rospy.Rate(.1)  # 20hz

        goal = ArmJointState(state)
        rospy.sleep(1)
        print('now publishing')
        pub.publish(goal)
        self._current_state = state
        # rate.sleep(2)


if __name__ == "__main__":
    robot = Robot("my cool robot")
