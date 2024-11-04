import os

image_name = input("Image name: ")

os.system(f"yolo task=detect mode=predict model=yolo11m.pt show=True conf=0.5 source={image_name}")
