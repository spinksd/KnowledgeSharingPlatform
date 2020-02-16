from django import template
register = template.Library()

# This is a custom filter used in page_form.html
# Firstly it checks that a list of tags has been passed in, if not it returns a blank string such that the placeholder for the input shows
# If tags do exist, it iterates through them and:
# 1. Checks if it's type string that's been passed in (this scenario occurs when the user enters an invalid form
# 1.1 If it is type string, keep the same value
# 2. If it's not type string, it's a tag. So add the tag names to a string, separated by commas
# This ensures that the tag input is presented with the correct tags in every scenario the user views the form
@register.filter
def form_tag_value_to_tags(tags):
    tags_string = ''
    if tags is not None:
        for tag in tags:
            if isinstance(tag, str):
                tags_string += tag
            else:
                tags_string += tag.name + ","
    return tags_string