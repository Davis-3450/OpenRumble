from app.core import VibeApp
from app.UI.gradio import UI_gradio
from app.UI.tk import run_gui


def main() -> None:
    vibe_app = VibeApp()

    user_input = input("Pick an option: 1. Gradio 2. Tkinter: ")
    if user_input == "1":
        UI_gradio(vibe_app).launch(share=True)
    elif user_input == "2":
        run_gui(vibe_app)
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
