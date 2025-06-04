import gradio as gr

# returns selected fruit
def handle_fruit(fruit):
	return f'selected fruit: {fruit}'

with gr.Blocks() as demo:
	fruit_dropdown = gr.Dropdown(label="Fruits", choices=['apple', 'orange', 'banana', 'melon'])
	output_fruit = gr.Textbox(label="Parchased Fruits")
	# shows selected fruits in the output
	fruit_dropdown.change(handle_fruit, inputs=fruit_dropdown, outputs=output_fruit)

demo.launch()