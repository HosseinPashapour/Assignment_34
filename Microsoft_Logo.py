import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image 

image = np.ones((650,1350,3), dtype=np.uint8) * 80

image[210:310 , 210:310] = (30 , 80  , 240)
image[210:310 , 320:420] = (0  , 180 , 120)
image[320:420 , 210:310] = (240, 160 , 0  )
image[320:420 , 320:420] = (0  , 180 , 255)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("input\Segoe UI.ttf", 160)
draw.text((470, 200), "Microsoft", font=font)
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

cv2.imshow("", image)
cv2.imwrite('output/Microsoft_logo.jpg', image)
cv2.waitKey()