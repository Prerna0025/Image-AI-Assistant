import gradio as gr

def process(user_text,img):
    return f"You typed: {user_text}\n Image size: {img.size if img else 'No image uploaded'}"

with gr.Blocks() as demo:
    gr.Markdown("Your Image Reading assistant")


    with gr.Row():
        
        txt_input = gr.Textbox(label="Enter your message")
        image_input = gr.Image(label="Upload and image",type="pil")
    
    submit_btn = gr.Button("Submit")
    output = gr.Textbox(label="Response")
    submit_btn.click(fn=process, inputs=[txt_input,image_input], outputs =output)
    #iface = gr.Interface(fn=greet, inputs="text",outputs="text")
demo.launch()