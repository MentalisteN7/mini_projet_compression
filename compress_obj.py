from obj_loader import ObjLoader

obj = 'bunny_origin.obj'

lapin = ObjLoader(obj)
print(lapin.vertices[lapin.faces[0][0]])
# 1.  Compute the Q matrices for all the initial vertices.

def Kp(a, b, c, d):
    return [[a*a, a*b, a*c, a*d],
            [a*b, b*b, b*c, b*d],
            [a*d, b*d, c*d, d*d]]

def planeEquation(A, B, C):
    a = (B[1] - A[1]) * (C[2] - A[2]) - (C[1] - A[1])*(B[2] - A[2])
    b = (B[2] - A[2]) * (C[0] - A[0]) - (C[2] - A[2])*(B[0] - A[0])
    c = (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0])*(B[1] - A[1])
    d = - (a*A[0] + b*A[1] + c*A[2])

    tot = (a + b + c + d)
    return (a/tot, b/tot, c/tot, d/tot)

a, b, c, d = planeEquation(lapin.vertices[lapin.faces[0][0]], lapin.vertices[lapin.faces[0][1]], lapin.vertices[lapin.faces[0][2]])
kp = Kp(a, b, c, d)
print(kp)
# 2.  Select all valid pairs.
# 3.  Compute the optimal contraction target Nv for each valid pair.v1;v2/. 
# The errorNvT.Q1CQ2/Nv of this target vertex becomes the cost of contracting that pair.
# 4.  Place all the pairs in a heap keyed on cost with the minimumcost pair at the top.
# 5.  Iteratively remove the pair.v1;v2/of least cost from the heap,contract this pair, and update the costs of all valid pairs involv-ingv1.