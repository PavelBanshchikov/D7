from django import template

register = template.Library()

@register.filter()
def censor(text):
    censor_words = {'редиска': 'р*******', 'дурак':'д****', 'идиот':'и****'}
    text_split = text.split()
    for i in range(len(text_split)):
        if text_split[i] in censor_words.keys():
            text_split[i] = censor_words[text_split[i]]
    text_censor = ' '.join(text_split)
    return text_censor
