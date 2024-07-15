from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
    
    def file_loader_1_change(self, file, **event_args):
        if file is not None:
            # Call the server function to classify the image and get annotated image
            annotated_image, predictions = anvil.server.call('classify_image', file)
            
            # Show the annotated image
            self.image_1.source = annotated_image
            
            # Display the predictions with percentages if confidence > 50%
            prediction_texts = [f"{pred['class']} ({pred['confidence']:.2%})" for pred in predictions]
            self.label_prediction.text = "Predictions: " + ", ".join(prediction_texts) if predictions else "No predictions with confidence > 50%"
