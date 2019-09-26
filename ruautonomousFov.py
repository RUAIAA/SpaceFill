import math

def imagingBox(positionX,positionY,altitude,cameraFovX,cameraFovY):
	spanX = math.tan(math.radians(cameraFovX/2)) * altitude
	spanY = math.tan(math.radians(cameraFovY/2)) * altitude

	xMin = positionX - spanX
	xMax = positionX + spanX
	yMin = positionY - spanY
	yMax = positionY + spanY

	return xMin,xMax,yMin,yMax
