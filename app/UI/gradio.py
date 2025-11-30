import gradio as gr

from app.core import VibeApp


def UI_gradio(app: VibeApp):
    with gr.Blocks() as gui:
        gr.Markdown("Vibe App")
        gr.Markdown("Select a pattern:")
        gr.Dropdown(
            choices=list(app.rumble.get_presets().keys()),
            value=list(app.rumble.get_presets().keys())[0],
        )
        gr.Button("Start", command=app.rumble.play_pattern)
        gr.Button("Stop", command=app.rumble.stop)
        gr.Text("Status:", value=app.rumble.status)

    return gui
