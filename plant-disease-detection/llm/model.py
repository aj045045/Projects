from torchvision import transforms
from PIL import Image
import torch

# Load your pretrained DL model
model = torch.load("plant_disease_model.pt")
model.eval()

def predict_disease(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        
    disease_classes = ['Apple___Scab', 'Apple___Black_rot', 'Corn___Blight']  # Example classes
    return disease_classes[predicted.item()]
