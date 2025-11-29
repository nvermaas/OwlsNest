from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def overnights(hike):
    # this is a tag that shows a line of overnight stays, coded in colors and icons

    wild_rough_nights_html = f"<i class='fas fa-campground' style='color: red;'></i> {hike.wild_rough_nights} " \
        if hike.wild_rough_nights else ""
    wild_campsite_nights_html = f"<i class='fas fa-campground' style='color: orange;'></i> {hike.wild_campsite_nights} " \
        if hike.wild_campsite_nights else ""
    campground_nights_html = f"<i class='fas fa-campground' style='color: green;'></i> {hike.campground_nights} " \
        if hike.campground_nights else ""
    indoor_nights_html = f"<i class='fa-solid fa-house' style='color: green;'></i> {hike.indoor_nights} " \
        if hike.indoor_nights else ""


    meta = f"<b>{hike.kilometers}</b> km in <b>{hike.days}</b> days. " if hike.kilometers else ""

    overnights_html = meta + wild_rough_nights_html + wild_campsite_nights_html + campground_nights_html + indoor_nights_html
    return mark_safe(overnights_html)

@register.simple_tag
def wild_rough_nights(nights):
    return mark_safe(f"<i class='fas fa-campground' style='color: red;'></i> {nights}")

@register.simple_tag
def wild_campsite_nights(nights):
    return mark_safe(f"<i class='fas fa-campground' style='color: yellow;'></i> {nights}")
