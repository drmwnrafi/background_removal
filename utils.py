import onnxruntime
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

class BackgroundRemover:
    def __init__(self, model):
        self.session = onnxruntime.InferenceSession(model, None)
        self.input_name = self.session.get_inputs()[0].name

    def preprocessing(self, img_path:str): 
        original_img = Image.open(img_path)
        img = original_img.resize((320, 320))
        img = np.array(img.convert('RGB'))
        img = np.expand_dims(img, axis=0) # Shape : (1, 320, 320,3)
        img = np.transpose(img, (0,3,1,2))
        img = img.astype(np.float32)
        img = img/255
        return original_img, img # Shape : (1, 3, 320, 320)
   
    def run_session(self, image):
        sess_input = {self.input_name:image}
        output = self.session.run(None, sess_input)[0] # Shape : (1, 3, 320, 320)
        return output
    
    def remove(self, img_path:str):
        og_img, inp = self.preprocessing(img_path)
        
        mask = self.run_session(inp)
        mask = mask.squeeze(axis = 0)
        mask = np.transpose(mask, (1,2,0))
        mask = mask[:,:,0] # Shape : (320, 320)
    
        mask = Image.fromarray((mask * 255).astype(np.uint8), "L").resize((og_img.size))
        empty = Image.new("RGBA", (og_img.size), 0)
        result = Image.composite(og_img, empty, mask)
        return result

