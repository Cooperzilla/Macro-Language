import pyautogui
from random import randint
from subprocess import run
from time import sleep

class macro:
    def __init__(self, file):
        self.file = open(file, "r").readlines()

    def run(self):
        for line in self.file:

            if line.startswith("startup/"):
                pass

            elif line.startswith("click/"):
                if line.split("/")[2] == "1":
                    pyautogui.click(button=line.split("/")[1])
                elif line.split("/")[2] == "2":
                    pyautogui.doubleClick(button=line.split("/")[1])

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
                        pyautogui.moveTo(pyautogui.position()[0], -1*int(line.split("/")[2])+pyautogui.position()[1])
                    elif line.split("/")[2] == "random":
                        try:
                            if line.split("/")[3] == "up":
                                pyautogui.moveTo(pyautogui.position()[0], randint(-1*pyautogui.position()[1], pyautogui.size()[1]))
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
                pyautogui.press(line.split("/")[1])

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

            elif line.startswith("scroll/"):
                 pyautogui.scroll(line.split('/')[1])

            elif line.startswith("mousedown"):
                pyautogui.mouseDown()

            elif line.startswith("mouseup"):
                pyautogui.mouseUp()

            elif line.startswith("keydown"):
                pyautogui.keyDown(line.split('/')[1])

            elif line.startswith("keyup"):
                pyautogui.keyeUp(line.split('/')[1])

            elif line.startswith("getscreen"):
                pyautogui.alert(text=f'x: {pyautogui.size()[0]} y: {pyautogui.size()[1]}', title='Screen size', button='OK')

            elif line.startswith("getpos"):
                pyautogui.alert(text=f'x: {pyautogui.position()[0]} y: {pyautogui.position()[1]}', title='Mouse pos', button='OK')

            elif line.startswith("alert/"):
                try:
                    pyautogui.alert(text=line.split('/')[2], title=line.split('/')[1], button=line.split('/')[3])
                except:
                    pyautogui.alert(text=line.split('/')[2], title=line.split('/')[1], button="Ok")

            elif line.startswith("start/"):
                pyautogui.hotkey("win", "r")
                pyautogui.typewrite(line.split("/")[1])
                pyautogui.press("enter")
