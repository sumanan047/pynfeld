from base import *

# This instanciates the pynfeld and runs the server
page = "index.html"
title = "Your Page"
navbar = "PYNFELD"
host = "127.0.0.1"
port = "8080"
ord_lst = ["Introduction", "Hello World", "First Example", "Second Example"]
section_dict ={"title": "1. Introduction", "paragraph": "The Pynfeld is a flask warpper that is supposed to produce quick static\
    pages that will quickly setup you with a server and pages. This can be used to generate quick documentations for \
        packages, turorials etc."}
theme = "maroon"
card_dict = {"card_image":"./static/images/doctor.jpeg",
"card_title":"Doctor Baby",
"paragraph":"Doctor is a nice boy who loves playing and cuddling with me. Doctor has a bark for everyone but as people come \
close, he only gives cuddles and kisses." }


# calling the instance with information

pynfeld = Pynfeld(page,title,navbar, host, port, True, app, theme=theme)
pynfeld.add_table(ord_lst)
pynfeld.add_section(section_dict)
pynfeld.add_card(card_dict)
pynfeld.run_page()