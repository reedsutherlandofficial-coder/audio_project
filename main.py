from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Header, Footer, Static, ContentSwitcher, DirectoryTree, Collapsible, Switch






class AudioDirectoryApp(App):
    CSS_PATH = "audioproject.tcss"
    TITLE = "Audio Info Loader"
    BINDINGS = [
                ("d", "toggle_dark", "Toggle Dark Mode"),
                ]
    
    def show_welcome(self):
        yield Welcome()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with Horizontal(id="buttons"):
            yield Button("WelcomeScreen", id="welcome_screen")
            yield Button("Directory", id="directory_picker")
            yield Button("File Format", id="file_format")
            
        with ContentSwitcher(initial="welcome_screen"):
            yield Static(
                "Welcome to the Audio Data Tool, use the top tabs to " \
                "navitage through each step of picking your files to " \
                "collect data from, and export them to desired format",
                id="welcome_screen")
            
            with Collapsible(title="Choose A Directory To Load", id="directory_picker"):
                yield DirectoryTree("./")

            with Static("Choose Audio Format", id ="file_format"):
                yield Horizontal(
                    Static("WAV:    ", classes="label"),
                    Switch(animate=True),
                    classes="container",
                )
                yield Horizontal(
                    Static("MP3:    ", classes="label"),
                    Switch(animate=True),
                    classes="container",
                )
                yield Horizontal(
                    Static("M4A:    ", classes="label"),
                    Switch(animate=True),
                    classes="container",
                )



    def on_button_pressed(self, event:Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id

    def on_mount(self) -> None:
        pass

        
        
    
    #def on_button_pressed(self) -> None:
        #pass #self.exit()

    def action_toggle_dark(self) -> None:
        self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )

if __name__ == "__main__":
    app = AudioDirectoryApp()
    app.run()