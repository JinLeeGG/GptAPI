import gradio as gr

# True / False value is inserted here 
def handle_checkbox(selected):
	if selected:
		# if true:
		return "Agreed"
	# if False
	return "Not Agreed"

with gr.Blocks() as demo:
	# creating checkbox in the web
	checkbox = gr.Checkbox(label="Do you consent to personal data gathering?")
	output_checkbox = gr.Textbox(label="Output")
	# If checkbox is cliked or unclicked --> returns True(selected) / False(unselected) 
	checkbox.change(handle_checkbox, inputs=checkbox, outputs=output_checkbox)

demo.launch()