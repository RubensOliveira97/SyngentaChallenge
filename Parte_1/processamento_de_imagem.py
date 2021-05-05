import cv2

#Get the picture of the challenge
syngenta_picture = cv2.imread("Syngenta.bmp")
#Clean the Syngenta Hire Me
clean_picture = cv2.inRange(syngenta_picture, (0,4,2),(66, 255, 160) )
#Count green dots(now white dots)
dots_number=cv2.countNonZero(clean_picture)
#Show response
print("Green dots number: {}".format(dots_number))
input("Pressione ENTER para Finalizar")
