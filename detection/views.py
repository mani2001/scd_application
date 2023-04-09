from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from tensorflow import keras
import cv2
import numpy as np
import json

# Create your views here.


def Welcome(request):
    return redirect('image_upload')
 
def surface_image_view(request):
 
    if request.method == 'POST':
        form = SurfaceForm(request.POST, request.FILES)
        surface = Surface()
        surface.surface_image = request.FILES['surface_image']
        image_path = str(surface.surface_image)
        request.session['image_path'] = json.dumps(image_path)
        if form.is_valid():
            form.save()
            return redirect('prediction')
    else:
        form = SurfaceForm()
    return render(request, 'surface_image_form.html', {'form': form})
 

def Prediction(request):
    prediction_var = ''
    model = keras.models.load_model('savedModels/mn_sc_weights.h5')
    path = 'media/images/{image_path}'.format(image_path=request.session['image_path'])
    path = path.replace('"','')
    img = cv2.imread(path)
    img = cv2.resize(img,(227,227))     # resize image to match model's expected sizing
    img = np.reshape(img,[1,227,227,3])
    pred = model.predict(img)
    print(pred)
    if(pred[0][0]>pred[0][1]):
        prediction_var = 'No Surface Crack/Cracks detected'
    else:
        prediction_var = 'Surface Crack/Cracks detected'
    return render(request,'prediction.html',{'prediction':prediction_var})