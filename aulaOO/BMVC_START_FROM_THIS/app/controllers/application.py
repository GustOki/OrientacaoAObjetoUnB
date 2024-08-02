from bottle import template, redirect


class Application():

    def __init__(self):

        self.pages = {
        }


    def render(self,page):
        content = self.pages.get(page, self.helper)
        return content()


    def helper(self):
        return template('app/views/html/helper')
