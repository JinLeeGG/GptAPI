import gradio as gr

# creating add function
def add(num1, num2):
	return num1 + num2

# Creating one screen
interface = gr.Interface(
	fn = add, # calling add function as call back
	# input two values
	inputs = ['number', 'number'],
	# return one value
	outputs = 'number',
	title = 'Calculator',
	description='Insert two seperate numbers',
	flagging_mode="never" # delete this for flagging (storing data in csv file)
)

interface.launch()