import gradio as gr

from app.core import VibeApp


def UI_gradio(app: VibeApp):
    presets = app.rumble.get_presets()
    choices = list(presets.keys())
    default_choice = choices[0] if choices else None

    def start_pattern(pattern_name: str) -> str:
        if not pattern_name:
            return "Status: error"
        pattern = app.rumble.get_presets().get(pattern_name)
        if not pattern:
            return "Status: error"
        app.rumble.play_pattern(pattern)
        return f"Status: {app.rumble.status} (Playing: {pattern_name})"

    def stop_pattern() -> str:
        app.rumble.stop()
        return f"Status: {app.rumble.status}"

    with gr.Blocks() as gui:
        gr.Markdown("# OpenRumble")
        gr.Markdown("Select a pattern and control the rumble")

        pattern_dropdown = gr.Dropdown(
            choices=choices,
            value=default_choice,
            label="Pattern",
        )

        status_text = gr.Textbox(
            label="Status", value=f"Status: {app.rumble.status}", interactive=False
        )

        with gr.Row():
            start_btn = gr.Button("Start")
            stop_btn = gr.Button("Stop")

        start_btn.click(fn=start_pattern, inputs=pattern_dropdown, outputs=status_text)
        stop_btn.click(fn=stop_pattern, outputs=status_text)

    return gui
