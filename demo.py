import cv2

#     READ AND DISPLAY IMAGES
#
# image = cv2.imread('art.jpg',1)
# cv2.imshow('image',image)
# cv2.waitKey(10000)
# cv2.imwrite('art.png',image)
# cv2.destroyAllWindows()

        # DRAW SHAPES

# image=cv2.imread('art.jpg',1)
# cv2.line(image,(0,0),(400,400),(255,0,0),5)
# cv2.imshow("shapes",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#           RECTANGLE
#
# image=cv2.imread('art.jpg',1)
# cv2.line(image,(0,0),(400,400),(255,0,0),5)
# cv2.rectangle(image,(0,0),(400,400),(0,255,0),3)
# cv2.imshow("shapes",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#             CIRCLE

# image=cv2.imread('art.jpg',1)
# cv2.line(image,(0,0),(400,400),(255,0,0),5)
# cv2.rectangle(image,(0,0),(400,400),(0,255,0),3)
# cv2.circle(image,(200,200),100,(0,0,255),-1)
# cv2.imshow("shapes",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

            # TEXT

image=cv2.imread('art.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(500,100),(0,255,0),3)
cv2.circle(image, (200, 200), 50, (0, 0, 255), -1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"hello",(100,100),font,3,(255,255,255),cv2.LINE_AA)
cv2.imshow("shapes",image)
cv2.waitKey(0)
cv2.destroyAllWindows()