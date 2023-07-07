from latex2svg import latex2svg
import base64
import xml.etree.ElementTree as ET


def encode(latex: str):
    """
    Encodes a LaTeX into svg
    Encodes a svg into base64.
    """
    svg = latex2svg(f"\({latex}\)")['svg']
    svg = color_white(svg)
    return svg2base64(svg)


def color_white(svg: str):
    # Parse the SVG string
    root = ET.fromstring(svg)

    # Find all path elements and change their fill color
    path_elements = root.findall(".//{http://www.w3.org/2000/svg}path")
    for path_element in path_elements:
        path_element.set("fill", "white")

    # Return the modified SVG as a string
    modified_svg = ET.tostring(root, encoding="unicode")
    return modified_svg


def svg2base64(svg_code: str):
    svg_bytes = svg_code.encode('utf-8')
    base64_encoded = base64.b64encode(svg_bytes)
    base64_string = base64_encoded.decode('utf-8')

    return base64_string
