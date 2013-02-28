from django.template import Template, Context

person = {'name': 'sally','sex': 'female'}
t = Template('{{person.name}}')
c = Context({'person': person})
t.render(c)
