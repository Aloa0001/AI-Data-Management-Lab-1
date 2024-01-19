def my_print(txt):  # positional arguments
    print(txt)


msg_template = """Hello {name},
thank you for joining our {website}. 
We are very happy to have you wwith us!
"""


def template_msg(name_="John", website_="abc.se"):  # keyword arguments
    return msg_template.format(name=name_, website=website_)
    # my_print(msg)
