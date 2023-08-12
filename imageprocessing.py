from PIL import Image  
#Open image using Image module  
im = Image.open("agri3.jpg")  
#Show actual Image  
im.show()  
#Show rotated Image  
imim = im.rotate(180)  
imim.show() 
