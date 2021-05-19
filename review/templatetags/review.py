from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def percent(value):
    return "{:d}%".format(round(100 * value))

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

"""
This is terrible, but for demoing purposes is here for now...
"""
@register.filter
def get_highestWith(dictionary, key):
    value = dictionary.get(key)
    if value != None:
        valuestr = str(value)
        return valuestr.split(" ")[3]
    else:
        return "N/A"

@register.filter
def get_avg(dictionary, key):
    value = dictionary.get(key).get("similarity__avg")
    if value == None:
        return 0
    else:
        return value

@register.filter
def get_max(dictionary, key):
    value = dictionary.get(key).get("similarity__max")
    if value == None:
        return 0
    else:
        return value


@register.inclusion_tag("review/_student.html")
def student_td(course, comparison, b=False):
    submission = comparison.submission_b if b else comparison.submission_a
    return {
        "url": reverse("comparison", kwargs={
            "course_key": course.key,
            "exercise_key": comparison.submission_a.exercise.key,
            "ak": comparison.submission_a.student.key,
            "bk": comparison.submission_b.student.key,
            "ck": comparison.pk }),
        "comparison": comparison,
        "submission": submission,
        "student": submission.student,
    }
