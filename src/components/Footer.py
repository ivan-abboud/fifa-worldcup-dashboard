from dash import html
from utils.theme import LINKEDIN


Footer = html.Div(html.H6(["©2022, Developed By ", html.A("Ivan Abboud" , href=LINKEDIN,style={"color": "#0084d6"})]), className="mt-9")