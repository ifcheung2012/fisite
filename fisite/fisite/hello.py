from django.template import Template, Context

person = {'name': 'sally'}
t = Template('{{person.name}}')
c = Context({'person': person})
t.render(c)
