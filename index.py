from libnya.colordescriptor import ColorDescriptor
import glob
import cv2
 
cd = ColorDescriptor((8, 12, 3))
output = open("index.csv", "w")
 
for imagePath in glob.glob("coba/*"):
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
 
	features = cd.describe(image)
 
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
 
output.close()