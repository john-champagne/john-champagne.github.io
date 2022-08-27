import svgwrite

dwg = svgwrite.Drawing('test.svg', profile='basic')

x_offset = 10
y_offset = 10

N_layers = 5

x_delta = 150
y_delta = 25

def t(*x):
    if isinstance(x,tuple):
        return (x[0][0]+x_offset,x[0][1]+y_offset)
    else:
        return (x[0]+x_offset, x[1]+y_offset)
    return None

def S(n,k):
    return (k>>(n-1)) & 0x1

def dependencies(n,k):
    if n==0:
        return set()
    s = S(n,k)
    dK = 2 ** (n-1)
    if s == 0:
        return set([(n-1,k+dK),(n-1,k)])
    else:
        return set([(n-1,k-dK),(n-1,k)])

def dependencies_recursive(X):
    
    for i in range(N_layers):
        old_X = X.copy()
        for x in old_X:
            d = dependencies(x[0],x[1])
            if d != None:
                X = X.union(d)
    return X

nodes = dict()
for i in range(N_layers):
    for j in range(2**(N_layers-1)):
        nodes[i,j] = (i*x_delta, j*y_delta)

active = dependencies_recursive(set([(4,6),(4,0)]))

# Draw Connections
for k in nodes:
    if k in active:
        deps = dependencies(k[0], k[1])
        if len(deps) > 0:
            dwg.add(dwg.line(t(nodes[deps.pop()]), t(nodes[k]), stroke=svgwrite.rgb(10, 10, 16, '%')))
            dwg.add(dwg.line(t(nodes[deps.pop()]), t(nodes[k]), stroke=svgwrite.rgb(10, 10, 16, '%')))


# Draw Nodes
for k in nodes:
    if k in active:
        p = t(nodes[k])
        dwg.add(dwg.circle(p,r=5,stroke="black", fill="white"))
    else:
        p = t(nodes[k])
        dwg.add(dwg.circle(p,r=5,stroke="black", fill="black"))
dwg.save()