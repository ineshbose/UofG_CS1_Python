def to_int(xy):
    return ord(xy[0])-ord('R'), ord(xy[1])-ord('R')

        

def load(font):
    glyphs = []
    with open("hershey-fonts/%s.jhf" % font) as f:
        for line in f:
            ix = int(line[0:5])        
            verts = int(line[5:8])        
            vx = [to_int(line[8 + 2*i:10+2*i]) for i in range(verts)]
            glyphs.append(vx)
    
    font = {}
    for ch in range(32,128):
        ix = ch - ord('A') + 33
        first = (-glyphs[ix][0][0],0,False)        
        ox, oy = 0,0
        rel = []
        pen_up = True
        for x,y in glyphs[ix][1:]:
            if x==-50:
                pen_up = True                
            else:
                if pen_up:
                    rel.append([x-ox, oy-y, False])
                    pen_up = False
                else:
                    rel.append([x-ox,oy-y, True])
                ox,oy = x,y
        last = (glyphs[ix][0][1]-ox,oy,False)
        font[chr(ch)] =  [first] + rel + [last]
        
    return font