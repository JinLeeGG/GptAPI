import gradio as gr

# creating a block
with gr.Blocks() as demo:
	gr.Markdown("# Hello World!")
	gr.Markdown("## Insert Subtitle here")
	gr.Markdown("- First item\n- Second item\n- Third item")

demo.launch()


