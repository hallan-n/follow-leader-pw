import time
import pyautogui
import pygetwindow as gw
import keyboard

from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED

class FollowLeader:
    def init(self):
        self.title = None
        self.x = None
        self.y = None

    def get_pw_windows(self, title: str):
        return gw.getWindowsWithTitle(title)
        
    def record_mouse(self):
        self.x, self.y = pyautogui.position()
        print(f'\n\nPosição do Lider da PT: {self.x}, {self.y}')
        print('Pressione F9 para todos seguir ele')
    
    def focus_window(self, window):
        try:
            if window.isMinimized:
                window.restore()
                time.sleep(0.1)
        except:
            pass
        try:
            window.activate()
            time.sleep(0.1)
        except:
            pass
        try:
            if not window.isActive:
                window.maximize()
                time.sleep(0.1)
                window.activate()
        except:
            pass


    def follow_leader(self):
        windows = self.get_pw_windows('The Classic PW')
        for window in windows:
            self.focus_window(window)
            time.sleep(1)
            pyautogui.doubleClick(self.x, self.y)

    def set_title(self):
        self.title = input("None do PW: ")



    

    def build_instructions_table(self) -> Table:
        table = Table(title="Atalhos", box=ROUNDED, show_edge=True, expand=False)

        table.add_column("Tecla", justify="center", style="bold yellow", no_wrap=True)
        table.add_column("Ação", style="bold white")

        table.add_row("F7", "Inserir nome da janela do PW")
        table.add_row("F8", "Gravar localização do líder da PT")
        table.add_row("F9", "Todos seguirem o líder")
        table.add_row("CTRL + C", "Sair do programa")
        return table    

    def main(self):
        console = Console()
        console.clear()
        console.print(self.build_instructions_table())
        keyboard.add_hotkey('F7', self.set_title)
        keyboard.add_hotkey('F8', self.record_mouse)
        keyboard.add_hotkey('F9', self.follow_leader)
        keyboard.wait()

FollowLeader().main()






# Exibe

