import pyautogui
from random import randint
from subprocess import run
from time import sleep
import PIL

class macro:
    def __init__(self, file):
        self.file = open(file, "r").readlines()

    def run(self):
        for line in self.file:

            if line.startswith("startup/"):
                pass

            elif line.startswith("click/"):
                if line.split("/")[1] == "1":
                    pyautogui.click()
                elif line.split("/")[1] == "2":
                    pyautogui.doubleClick()

            elif line.startswith("move/"):
                if line.split("/")[1] == "x":
                    if not line.split("/")[2] == "random":
                        pyautogui.moveTo(int(line.split("/")[2])+pyautogui.position()[0], pyautogui.position()[1])
                    elif line.split("/")[2] == "random":
                        try:
                            if line.split("/")[3] == "left":
                                pyautogui.moveTo(randint(pyautogui.position()[0], pyautogui.size()[0]), pyautogui.position()[1])
                            elif line.split("/")[3] == "right":
                                pyautogui.moveTo(randint(-1*(pyautogui.size()[0]-pyautogui.position()[0]), pyautogui.position()[0]), pyautogui.position()[1])
                        except:
                            pyautogui.moveTo(randint(-1*(pyautogui.size()[0]-pyautogui.position()[0]), pyautogui.size()[0]), pyautogui.position()[1])
                elif line.split("/")[1] == "y":
                    if not line.split("/")[2] == "random":
                        pyautogui.moveTo(pyautogui.position()[0], int(line.split("/")[2])+pyautogui.position()[1])
                    elif line.split("/")[2] == "random":
                        try:
                            if line.split("/")[3] == "up":
                                pyautogui.moveTo(pyautogui.position()[0], randint(-pyautogui.position()[1], pyautogui.size()[1]))
                            elif line.split("/")[3] == "down":
                                pyautogui.moveTo(pyautogui.position()[0], randint(-1*(pyautogui.size()[1]-pyautogui.position()[1]), pyautogui.position()[1]))
                        except:
                            pyautogui.moveTo(pyautogui.position()[0], randint(-1*(pyautogui.size()[1]-pyautogui.position()[1]), pyautogui.size()[1]))
                elif line.split("/")[1] == "random":
                    try:
                        if line.split("/")[3] == "left":
                            pyautogui.moveTo(randint(pyautogui.position()[0], pyautogui.size()[0]), pyautogui.position()[1])
                        elif line.split("/")[3] == "right":
                            pyautogui.moveTo(randint(-1*(pyautogui.size()[0]-pyautogui.position()[0]), pyautogui.position()[0]), pyautogui.position()[1])
                        elif line.split("/")[2] == "up":
                            pyautogui.moveTo(pyautogui.position()[0], randint(-pyautogui.position()[1], pyautogui.size()[1]))
                        elif line.split("/")[2] == "down":
                            pyautogui.moveTo(pyautogui.position()[0], randint(-1*(pyautogui.size()[1]-pyautogui.position()[1]), pyautogui.position()[1]))
                    except:
                         pyautogui.moveTo(randint(-1*(pyautogui.size()[0]-pyautogui.position()[0]), pyautogui.size()[0]), randint(-1*(pyautogui.size()[1]-pyautogui.position()[1]), pyautogui.size()[1]))

            elif line.startswith("execute/"):
                run([line.split("/")[1].spiit(" ")], shell=True)

            elif line.startswith("key/"):
                pyautogui.keyDown(line.split("/")[1])
                pyautogui.keyUp(line.split("/")[1])

            elif line.startswith("type/"):
                pyautogui.typewrite(line.split("/")[1])

            elif line.startswith("//") or line.startswith("#"):
                pass

            elif line.startswith("goto/"):
                pyautogui.moveTo(line.split("/")[1], line.split("/")[2])

            elif line.startswith("setpos/"):
                if line.split("/") == "x":
                    pyautogui.moveTo(int(line.split("/")[2]), pyautogui.position()[1])
                elif line.split("/") == "y":
                    pyautogui.moveTo(pyautogui.position()[0], int(line.split("/")[2]))

            elif line.startswith("hotkey/"):
                pyautogui.hotkey(line.split("/")[1], line.split("/")[2])

            elif line.startswith("copy"):
                pyautogui.hotkey("ctrl", "c")

            elif line.startswith("paste"):
                pyautogui.hotkey("ctrl", "v")

            elif line.startswith("wait/"):
                sleep(int(line.split("/")[1]))

            elif line.startswith("cut"):
                pyautogui.hotkey("ctrl", "x")

            elif line.startswith("undo"):
                pyautogui.hotkey("ctrl", "z")

            elif line.startswith("redo"):
                pyautogui.hotkey("ctrl", "y")

            elif line.startswith("selectall"):
                pyautogui.hotkey("ctrl", "a")

            elif line.startswith("delete"):
                pyautogui.hotkey("ctrl", "d")

            elif line.startswith("screenshot/"):
                 pyautogui.screenshot(line.split('/')[1].strip())


