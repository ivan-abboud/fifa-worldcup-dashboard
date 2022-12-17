from dash import html
from utils.consts import LINKEDIN_PROFILE


Footer = html.Div(html.H6(["©2022, Developed By ", html.A("Ivan Abboud" , href=LINKEDIN_PROFILE, target="_blank",style={"color": "#0084d6"})]), className="mt-9")