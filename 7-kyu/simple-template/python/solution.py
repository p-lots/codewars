import re

def create_template(template):
    def template_maker(**replacements):
        return re.sub('{{(?P<word>\w+)}}', lambda m: replacements.get(m.group('word'), ''), template)
    return template_maker
