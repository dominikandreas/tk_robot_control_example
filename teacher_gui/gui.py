from tkinter import Tk, Frame, Button, Label, Text, Spinbox, END
from teacher_gui.robot import Robot


class JointControlButton:
    def __init__(self, master, text, step_size, callback, column, row):
        self.step_size = step_size
        self.callback = callback
        self.btn = Button(master, text=text, command=self.move)
        self.btn.grid(column=column, row=row)

    def move(self):
        self.callback(self.step_size)


class JointControl(Frame):
    def __init__(self, master, name, index, robot, min_step, max_step, step_size, **options):
        super().__init__(master, **options)
        self.name = name
        self.index = index
        self.robot = robot
        self.label_name = Label(master, text=name + ": ").grid(column=0, row=index)

        self.spin_box_steps = Spinbox(master, from_=min_step, to=max_step)  # Anzahl der Schritte eingeben
        self.spin_box_steps.grid(column=1, row=index)  # Spin Box Position festlegen

        self.button_accept_position = Button(master, text=name + " Position uebernehmen",
                                             command=self.accept_position)
        self.button_accept_position.grid(column=1, row=index)

        self.label_current_pos = Label(master, text=name + " Aktuelle Position: ").grid(column=3, row=index)
        self.text_pos = Text(master, height=1, width=20)
        self.text_pos.grid(column=4, row=index)
        self.text_pos.insert("1.0", self.robot.current_state[self.index])

        self.step_buttons = []
        for list_index, step in enumerate([-step_size, step_size, -step_size*5, step_size*5]):
            text = "Aktuelle Position " + ("" if step < 0 else "+") + str(step)
            button = JointControlButton(master, text, step, column=5 + list_index, row=index, callback=self.move)
            self.step_buttons.append(button)

    def update_text(self, content):
        self.text_pos.delete("1.0", END)
        self.text_pos.insert("1.0", content)

    def move(self, steps):
        old_pos = self.robot.current_state[self.index]
        self.robot.set_joint(self.index, old_pos + steps)
        self.update_text(self.robot.current_state[self.index])

    def accept_position(self):
        steps = int(self.spin_box_steps.get())
        print(self.name + "Schritte: " + str(steps))
        self.robot.set_joint(self.index, steps)


class RobotControlGui(Tk):
    def __init__(self, robot):
        super().__init__()
        self.title("Position Teacher app")
        self.geometry('1500x1500')
        self.robot = robot
        self.joint_controls = []

        self.add_joint_control("Greifer", 5, min_step=0, max_step=70, step_size=1)
        self.add_joint_control("5. Achse", 4, min_step=-1000, max_step=1000, step_size=10)
        self.add_joint_control("4. Achse", 3, min_step=-1000, max_step=1000, step_size=10)
        self.add_joint_control("3. Achse", 2, min_step=-1000, max_step=1000, step_size=100)
        self.add_joint_control("2. Achse", 1, min_step=-1000, max_step=1000, step_size=10)
        self.add_joint_control("1. Achse", 1, min_step=-1000, max_step=1000, step_size=10)

    def add_joint_control(self, name, index, min_step, max_step, step_size):
        self.joint_controls.append(JointControl(self, name, index, self.robot, min_step, max_step, step_size))


if __name__ == "__main__":
    my_robot = Robot(name="Moveo 2000 Mk II")
    gui = RobotControlGui(my_robot)
    gui.mainloop()
