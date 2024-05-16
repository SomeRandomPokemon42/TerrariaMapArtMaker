import TerrariaBlockset


def Vector3Distance(vector1, vector2):
	vector3 = (vector1[0] - vector2[0], vector1[1] - vector2[1], vector1[2] - vector2[2])
	if vector3[0] < 0:
		vector3 = (-vector3[0], vector3[1], vector3[2])
	if vector3[1] < 0:
		vector3 = (vector3[0], -vector3[1], vector3[2])
	if vector3[2] < 0:
		vector3 = (vector3[0], vector3[1], -vector3[2])
	return vector3[0] + vector3[1] + vector3[2]

def GetClosestColorInt(DesiredColor, blockset = TerrariaBlockset.Blockset):
	closestColor = (0,0,0)
	colorDistance = 999
	for color in blockset.keys():
		colorDist = Vector3Distance(color, DesiredColor)
		if colorDist < colorDistance:
			colorDistance = colorDist
			closestColor = color
	return closestColor


def GetClosestColor(DesiredColor, blockset = TerrariaBlockset.Blockset):
	return blockset[GetClosestColorInt(DesiredColor, blockset)]