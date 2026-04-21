from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Header, Footer, Static, ContentSwitcher, DirectoryTree, Collapsible, Switch, Label
from pathlib import Path
from typing import Iterable



class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")]

class AudioDirectoryApp(App):
    CSS_PATH = "audioproject.tcss"
    TITLE = "Audio Info Loader"
    BINDINGS = [
                ("d", "toggle_dark", "Toggle Dark Mode"),
                ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with Horizontal(id="buttons_left"):
            yield Button("Welcome", id="welcome_screen")
            yield Button("Directory", id="directory_picker")
            
        with ContentSwitcher(initial="welcome_screen"):
            yield Static(
                "Welcome to the Audio Data Tool, use the top tabs to " \
                "navitage through each step of picking your files to " \
                "collect data from, and export them to desired format",
                id="welcome_screen")
            
            with Collapsible(title="Choose A Directory To Load", id="directory_picker"):
                yield FilteredDirectoryTree("~")
                yield Button("Pick Directory", id="pick_directory")

                def on_file_selected(self) -> None:
                    pass
                def on_button_pressed(self) -> None:
                    pass

        
        with Horizontal(id="buttons_right"):
            yield Button("File Format", id="file_format")
            yield Button("Export", id ="export")

        with ContentSwitcher(initial="file_format"):
            yield Label("Choose Audio Format", id="file_format")
            yield Horizontal(
                Static("WAV:    ", classes="label"),
                Switch(animate=True),
                classes="container",
                id="wav_button"
            )
            yield Horizontal(
                Static("MP3:    ", classes="label"),
                Switch(animate=True),
                classes="container",
                id="mp3_button"
            )
            yield Horizontal(
                Static("M4A:    ", classes="label"),
                Switch(animate=True),
                classes="container",
                id="m4a_button"
            )
            with Collapsible(title="Export To Path", id="export"):
                yield FilteredDirectoryTree("~", id= "folder_choice")
                yield Button("Save", id="pressed_save")

                def on_file_selected(self) -> None:
                    pass
                def on_button_pressed(self) -> None:
                    pass

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def on_button_pressed(self, event:Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id

    
    

        
        
    
    #def on_button_pressed(self) -> None:
        #pass #self.exit()

    def action_toggle_dark(self) -> None:
        self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )

if __name__ == "__main__":
    app = AudioDirectoryApp()
    app.run()