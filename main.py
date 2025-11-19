import time
import pyautogui
import pygetwindow as gw
import keyboard

from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED

class FollowLeader:
    console = Console()
    x = None
    y = None
    leader = None


    def set_leader_window(self):
        self.leader = gw.getActiveWindow()
        self.show_instructions()
        print('lider', self.leader._hWnd)

    def get_pw_windows(self, title: str):
        return gw.getWindowsWithTitle(title)
        
    def record_mouse(self):
        self.x, self.y = pyautogui.position()
        self.show_instructions()

    def focus_window(self, window):
        window.restore()
        time.sleep(0.1)
        window.activate()


    def follow_leader(self):
        windows = self.get_pw_windows(self.leader.title)
        for window in windows:
            self.focus_window(window)
            
            time.sleep(0.1)
            pyautogui.tripleClick(self.x, self.y)
            time.sleep(0.1)
            pyautogui.tripleClick(self.x, self.y)

        self.focus_window(self.leader)


    def build_instructions_table(self) -> Table:
        table = Table(title="Atalhos", box=ROUNDED, show_edge=True, expand=False)

        table.add_column("Tecla", justify="center", style="bold yellow", no_wrap=True)
        table.add_column("Ação", style="bold white")
        table.add_column("Valor atual", style="bold red")
        
        table.add_row("F7", "Selecione a janela do lider da PT", "Selecionado" if self.leader else "Aguardando")
        table.add_row("F8", "Gravar localização do líder da PT", f"{self.x}, {self.y}" if self.x else "Aguardando")
        table.add_row("F9", "Todos seguirem o líder", "-")
        table.add_row("CTRL + C", "Sair do programa", "-")
        return table    

    def show_instructions(self):
        self.console.clear()
        self.console.print(self.build_instructions_table())

    def main(self):
        self.show_instructions()
        keyboard.add_hotkey('F7', self.set_leader_window)
        keyboard.add_hotkey('F8', self.record_mouse)
        keyboard.add_hotkey('F9', self.follow_leader)
        keyboard.wait()

FollowLeader().main()
