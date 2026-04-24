from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.events import Click
from textual.widgets import Button, Header, Footer, Static, ContentSwitcher, DirectoryTree, Collapsible, Switch, Label, ListItem
from pathlib import Path
from typing import Iterable
from audiofuncs import Audioprocess

class Data():
     inpath = []
     outpath = []

data = Data()

class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")]
    
#class Clickablefile(DirectoryTree):
     #def _on_click(self, File_selected, event: Click) -> None:
          #if event.chain == 2:
               #print(File_selected.path, "double clicked file!")

class AudioDirectoryApp(App):
    CSS_PATH = "audioproject.tcss"
    TITLE = "Audio Info Loader"
    BINDINGS = [
                ("d", "toggle_dark", "Toggle Dark Mode"),
                ]
    
    def on_directory_tree_file_selected(self, File_Selected) -> None:
        data.inpath.append(File_Selected.path)
        print(data.inpath)
        
    def on_button_pressed_for_process_button(self, event:Button.Pressed, id="process_button") -> None:
        Audioprocess(data.inpath).visuals
            
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id
        Audioprocess(data.inpath).visuals

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def action_toggle_dark(self) -> None:
        self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with Horizontal(id="buttons"):
            yield Button("Welcome", id="welcome_screen")
            yield Button("Directory", id="directory_picker")
            yield Button("File Format", id="file_format")
            yield Button("Export", id="export_menu")
            yield Button("Process", id="process_button")

        with ContentSwitcher(initial="welcome_screen"):
            yield Static(
                "Welcome to the Audio Data Tool, use the top tabs to " \
                "navitage through each step of picking your files to " \
                "collect data from, and export them to desired format",
                id="welcome_screen")
            
            with Collapsible(title="Choose A Directory To Load", collapsed=False, id="directory_picker"):
                yield FilteredDirectoryTree("~")
                
            with Label("Choose Audio Format", expand=True, id="file_format"):
                yield Horizontal(
                    Static("WAV:    ", classes="label"),
                    Switch(animate=True),
                    classes="container",
                    id="wav_switch"
                )
                yield Horizontal(
                    Static("MP3:    ", classes="label"),
                    Switch(animate=True),
                    classes="container",
                    id="mp3_switch"
                )
                yield Horizontal(
                    Static("M4A:    ", classes="label"),
                    Switch(animate=True),
                    classes="container",
                    id="m4a_switch"
                )
            yield Static("Exported", classes="label", id="process_button")

                #Audioprocess.visuals
                # have a "process" button, which 
                # calls librosal with selected audio format and data.path, and use some convert function there 
                # 
            with Collapsible(title="Export To Path", collapsed=False, id="export_menu"):
                yield Button("Save", id="pressed_save")
                yield FilteredDirectoryTree("~", id="folder_choice")
            
                def on_file_selected(self) -> None:
                    pass
                
   

if __name__ == "__main__":
    app = AudioDirectoryApp()
    app.run()