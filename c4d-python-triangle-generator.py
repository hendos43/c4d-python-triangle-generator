#This script creates a triangular polygon with a base length of 1
#input the three angles of your triangle and this will generate the triangle for you

import c4d
import math

def main():

 #--SPECIFY ANGLES IN DEGREES HERE:--
 angleAdeg = 90
 angleBdeg = 45
 angleCdeg = 45
  #--END USER INPUT--

 #convert degrees to radians for each
 angleA = math.radians(angleAdeg)
 angleB = math.radians(angleBdeg)
 angleC = math.radians(angleCdeg)

 #assuming AB (called c) has length of 1
 c = 1
 #calculate length of BC (called a)
 a = c *(math.sin(angleA)/math.sin(angleC))
 #calculate length of AC (called b)
 b = c *(math.sin(angleB)/math.sin(angleC))
 #calculate area
 area = (a * b * math.sin(angleC))/2
 #calculate height of triangle
 #this will be the y co-ordinate of the third point of the triangle
 hc = (2*area)/c
 #find the x-coordinate using a right angled triangle with height hc, and the component angle C
 componentC = 180 - 90 - angleAdeg
 componentC = math.radians(componentC)
 #ignore dividing by sin(90) since = 1
 xcoord = b*math.sin(componentC)

 mypoly = c4d.BaseObject(c4d.Opolygon) #Create an empty polygon object
 mypoly.ResizeObject(3,1) #New number of points, New number of polygons

 mypoly.SetPoint(0,c4d.Vector(0,0,0))
 mypoly.SetPoint(1,c4d.Vector(1,0,0))
 mypoly.SetPoint(2,c4d.Vector(xcoord,hc,0))


 mypoly.SetPolygon(0, c4d.CPolygon(0, 1, 2) ) #The Polygon's index, Polygon's points

 doc.InsertObject(mypoly,None,None)
 mypoly.Message(c4d.MSG_UPDATE)

 c4d.EventAdd()

if __name__=='__main__':
 main()