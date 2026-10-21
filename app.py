import gradio as gr
from transformers import pipeline

# Load the pipeline
generator = pipeline("text-generation", model="gpt2")

# Define the function to use in Gradio
def generate_text(prompt):
    output = generator(prompt, max_length=50, num_return_sequences=1)
    return output[0]['generated_text']

# Gradio interface
gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, label="Enter Prompt"),
    outputs=gr.Textbox(label="Generated Text"),
    title="Text Generator using GPT-2"
).launch()