import gradio as gr

# returns text 
def handle_input(text):
	return text

with gr.Blocks() as demo:
	# creating a input text box
	# line = 1 (user can only insert one line)
	# input data is stored in text_input
	text_input = gr.Textbox(label = "insert text", lines=1) 
	
	# creating a output text box 
	output_text = gr.Textbox(label = "Output")

	# input value in input textbox --> submitting output text box
	text_input.submit(handle_input, inputs=text_input, outputs=output_text)

demo.launch()