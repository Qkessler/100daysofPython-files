from functools import wraps


def make_html(element):
    def real_decorator(function):
        @wraps(function)
        def wrapper(text):
            string_r = "<"+element+">"
            string_r += function(text)
            string_r += "</"+element+">"
            return string_r
        return wrapper
    return real_decorator

@make_html('p')
@make_html('h1')
def get_text(text='Esto es el texto default'):
    return text

print(get_text('Creacion'))
