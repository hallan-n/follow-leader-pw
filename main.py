import time
import pyautogui
import pygetwindow as gw
import keyboard

from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED

class FollowLeader:
    console = Console()
    title = None
    x = None
    y = None

    def get_pw_windows(self, title: str):
        return gw.getWindowsWithTitle(title)
        
    def record_mouse(self):
        self.x, self.y = pyautogui.position()
        self.show_instructions()
    
    def focus_window(self, window):
        try:
            if window.isMinimized:
                window.restore()
                time.sleep(0.1)
        except: pass
        try:
            window.activate()
            time.sleep(0.1)
        except: pass
        try:
            if not window.isActive:
                window.maximize()
                time.sleep(0.1)
                window.activate()
        except: pass


    def follow_leader(self):
        windows = self.get_pw_windows('The Classic PW')
        for window in windows:
            self.focus_window(window)
            time.sleep(1)
            pyautogui.doubleClick(self.x, self.y)

    def set_title(self):
        self.title = input("Nome da janela do PW: ").strip()
        self.show_instructions()

    def build_instructions_table(self) -> Table:
        table = Table(title="Atalhos", box=ROUNDED, show_edge=True, expand=False)

        table.add_column("Tecla", justify="center", style="bold yellow", no_wrap=True)
        table.add_column("Ação", style="bold white")
        table.add_column("Valor atual", style="bold red")

        table.add_row("F7", "Inserir nome da janela do PW", self.title or "Aguardando")
        table.add_row("F8", "Gravar localização do líder da PT", f"{self.x}, {self.y}" if self.x else "Aguardando")
        table.add_row("F9", "Todos seguirem o líder", "Aguardando")
        table.add_row("CTRL + C", "Sair do programa", "Aguardando")
        return table    

    def show_instructions(self):
        self.console.clear()
        self.console.print(self.build_instructions_table())

    def main(self):
        self.show_instructions()
        keyboard.add_hotkey('F7', self.set_title)
        keyboard.add_hotkey('F8', self.record_mouse)
        keyboard.add_hotkey('F9', self.follow_leader)
        keyboard.wait()

FollowLeader().main()
