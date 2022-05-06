import rhinoscriptsyntax as rs
import random
import math

def Cube(Center,width,length,height):
    
    Cx = Center[0]
    Cy = Center[1]
    Cz = Center[2]
    
    #bottom of the cube
    p1 = (Cx-width,Cy-length,Cz-height)
    p2 = (Cx+width,Cy-length,Cz-height)
    p3 = (Cx+width,Cy+length,Cz-height)
    p4 = (Cx-width,Cy+length,Cz-height)
    
    #top of the cube
    p5 = (Cx-width,Cy-length,Cz+height)
    p6 = (Cx+width,Cy-length,Cz+height)
    p7 = (Cx+width,Cy+length,Cz+height)
    p8 = (Cx-width,Cy+length,Cz+height)
    
    Box = rs.AddBox([p1,p2,p3,p4,p5,p6,p7,p8])
    
    return(Box)

#Input number of boxes and the step(space between)
count = rs.GetInteger("enter number of boxes")
step = rs.GetInteger("enter distance between each box")

#Gives box dimensions
for i in range(0,count,step):
    w = random.uniform(5.0,20.0) #width
    l = random.uniform(10.0,30.0) #length
    h = random.uniform(5.0,20.0) #height
    Cube((i,0,0),w,l,h)

y = rs.GetInteger("enter number of times to rotate")
for n in range(y):
    objs = rs.GetObjects("select objects to rotate")
    p = rs.GetPoint("pick point")
    j = random.uniform(10.0,45.0)
    r = rs.RotateObjects(objs, p, j)

z = rs.GetInteger("enter number of times to move")
for m in range(z):
    obj2 = rs.GetObjects("Select objects to move")
    start = rs.GetPoint("Point to move from")
    end = rs.GetPoint("Point to move to")
    translation = end-start
    rs.MoveObjects(obj2, translation)

bool = rs.Command("BooleanSplit")

def move_in(objects,distance, point):
    off_set = rs.OffsetCurve( objects, point , distance )

    return off_set

def move_objects_out(site_boundary, objects):

    centroid = rs.AddPoint(rs.SurfaceAreaCentroid(site)[0])

    edgecurves = rs.DuplicateSurfaceBorder(site)
    off_set = move_in(edgecurves, 40, centroid)

    edgepoints = rs.DivideCurve(off_set, len(objects))
    vectors = []
    for i in edgepoints:
        vectors.append(rs.VectorCreate(centroid,i))
    for j in range(len(objects)):
        rs.MoveObject(objects[j],vectors[j])

def move_objects_out2(site_boundary, objects):

    centroid = rs.AddPoint(rs.SurfaceAreaCentroid(site)[0])

    edgecurves = rs.DuplicateSurfaceBorder(site)
    off_set = move_in(edgecurves, 60, centroid)

    edgepoints = rs.DivideCurve(off_set, len(objects))
    vectors = []
    for i in edgepoints:
        vectors.append(rs.VectorCreate(centroid,i))
    for j in range(len(objects)):
        rs.MoveObject(objects[j],vectors[j])

srf = rs.GetObject("select site to dup")
db = rs.DuplicateSurfaceBorder(srf)

site = rs.GetObject("select the site")

objects = rs.GetObjects("select masses")
move_objects_out(site, objects)

rs.Command("ChangeLayer")

#A = rs.GetObjects("Select massings to add color")
#Color1 = rs.GetColor(0) 
#rs.AddMaterialToObject(A)  
#Index = rs.ObjectMaterialIndex(A)
#rs.MaterialColor(Index,Color1)

srf2 = rs.GetObject("select site to dup")
db2 = rs.DuplicateSurfaceBorder(srf2)

site2 = rs.GetObject("select the site")

objects2 = rs.GetObjects("select masses")
move_objects_out2(site2, objects2)


rs.Command("Move")
crv = rs.Command("SelCrv")
rs.Command("Delete")