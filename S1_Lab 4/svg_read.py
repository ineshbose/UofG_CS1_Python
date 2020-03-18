from lxml import etree
import re

def parse_path(path):
    # parse the path elements in an SVG path
    # only handles straight line elements
    elts = path.split()
    pts = []
    px, py = 0,0
    for elt in elts:                
        xy = elt.split(",")
        if len(xy)==2:
            x, y = float(xy[0]), float(xy[1])
            px += x
            py += -y
            pts.append((px,py))   
    return pts
        
def find_paths(fname):
    # find all paths in the SVG document, and return the points that make up their elements
    # ignore bezier curves for the moment
    xml = etree.parse(fname)
    paths = []
    for element in xml.iter():
        if element.tag.endswith("}path"):            
            paths.append(parse_path(element.get("d")))
    return paths


    