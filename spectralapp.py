from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container
from textual.events import Click
from textual.widgets import Button, Header, Footer, Static, ContentSwitcher, DirectoryTree, Collapsible, Switch, Label, ListItem
from pathlib import Path
from typing import Iterable
from audiofuncs import Audioprocess

class Data():
     #temppath = []
     inpath = []
     outpath = []

data = Data()

class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")]


class Spectralapp(App):
    CSS_PATH = "audioproject.tcss"
    TITLE = "Spectral"
    BINDINGS = [
                ("d", "toggle_dark", "Toggle Dark Mode"),
                ]
    
    def on_directory_tree_file_selected(self, path) -> None:
            data.inpath.append(path.path)
            print(data.inpath)

    @on(Button.Pressed, "#process_button")
    def process_button(self) -> None:
        Audioprocess(data.inpath)
    
    @on(Button.Pressed, "#exit_button")
    def exit_button(self) -> None:
        App.exit(self)
        
    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def action_toggle_dark(self) -> None:
        self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with Horizontal(id="directory"):
            yield FilteredDirectoryTree("~")
        yield Container(        
             Horizontal(
                        Button("Process", id="process_button"),
                        Button("Exit", id= "exit_button"), classes = "buttons"
                        ) 
                        ,id="button_container"
        )

        
                
                
if __name__ == "__main__":
    app = Spectralapp()
    app.run()
    import sys
    sys.exit(app.return_code or 0)