import os
import time

import pyautogui
import pygetwindow as gw
from pynput import keyboard

positions = None
leader = None
title = None


def load_menu():
    os.system("cls")

    print(
        f"""
Menu Principal

(F7)  Definir líder da PT  [{"✅" if leader else "❌"}]
(F8)  Definir posição X e Y [{"✅" if positions else "❌"}]
(F9)  Clicar
(F10) Sair

Título: {title or "-"}

"""
    )


def set_leader_window():
    global leader
    global title
    leader = gw.getActiveWindow()
    title = leader.title
    load_menu()


def get_pw_windows(title: str):
    return gw.getWindowsWithTitle(title)


def record_mouse():
    global positions
    x, y = pyautogui.position()
    positions = x, y
    load_menu()


def focus_window(window):
    window.restore()
    time.sleep(0.1)
    window.activate()


def follow_leader():
    global positions
    global leader

    windows = get_pw_windows(leader.title)
    for window in windows:
        focus_window(window)
        time.sleep(0.1)
        pyautogui.tripleClick(positions[0], positions[1])
        time.sleep(0.1)
        pyautogui.tripleClick(positions[0], positions[1])

    focus_window(leader)


def main():
    def on_press(key):
        if key == keyboard.Key.f7:
            set_leader_window()
            load_menu()

        elif key == keyboard.Key.f8:
            record_mouse()
            load_menu()

        elif key == keyboard.Key.f9:
            follow_leader()
            load_menu()

        elif key == keyboard.Key.f10:
            print("Até mais o/")
            return False

    load_menu()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
