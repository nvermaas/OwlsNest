from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def overnights(hike):
    # this is a tag that shows a line of overnight stays, coded in colors and icons

    wild_rough_nights_html = f"<i class='fas fa-campground' style='color: red;'></i> {hike.wild_rough_nights} &nbsp;" \
        if hike.wild_rough_nights else ""
    wild_campsite_nights_html = f"<i class='fas fa-campground' style='color: orange;'></i> {hike.wild_campsite_nights} &nbsp; " \
        if hike.wild_campsite_nights else ""
    campground_nights_html = f"<i class='fas fa-campground' style='color: green;'></i> {hike.campground_nights}  &nbsp;" \
        if hike.campground_nights else ""
    indoor_refuge_html = f"<i class='fa-solid fa-house' style='color: red;'></i> {hike.indoor_refuge} &nbsp; " \
        if hike.indoor_refuge else ""
    indoor_unstaffed_html = f"<i class='fa-solid fa-house' style='color: orange;'></i> {hike.indoor_unstaffed} &nbsp; " \
        if hike.indoor_unstaffed else ""
    indoor_staffed_html = f"<i class='fa-solid fa-house' style='color: green;'></i> {hike.indoor_staffed} &nbsp; " \
        if hike.indoor_staffed else ""

    meta = f"<b>{hike.kilometers}</b> km in <b>{hike.days}</b> days. &nbsp; " if hike.kilometers else ""

    overnights_html = meta + wild_rough_nights_html + wild_campsite_nights_html + campground_nights_html + \
                      indoor_refuge_html + indoor_unstaffed_html + indoor_staffed_html
    return mark_safe(overnights_html)

@register.simple_tag
def overnights_selected_hikes(hikes):
    # this is a tag that shows a line of overnight stays, coded in colors and icons, for the selected hikes
    days = 0
    kilometers = 0

    wild_rough_nights = 0
    wild_campsite_nights = 0
    campground_nights = 0
    indoor_refuge = 0
    indoor_unstaffed = 0
    indoor_staffed = 0

    for hike in hikes:
        days += hike.days if hike.days else days
        kilometers += hike.kilometers if hike.kilometers else kilometers

        wild_rough_nights += hike.wild_rough_nights
        wild_campsite_nights += hike.wild_campsite_nights
        campground_nights += hike.campground_nights
        indoor_refuge += hike.indoor_refuge
        indoor_unstaffed += hike.indoor_unstaffed
        indoor_staffed += hike.indoor_staffed

    wild_rough_nights_html = f"<i class='fas fa-campground' style='color: red;' data-bs-toggle='tooltip' data-bs-placement='top' title='wild camping'></i> {wild_rough_nights} &nbsp;" \
        if wild_rough_nights else ""
    wild_campsite_nights_html = f"<i class='fas fa-campground' style='color: orange;' data-bs-toggle='tooltip' data-bs-placement='top' title='wildernis campsite'></i> {wild_campsite_nights} &nbsp; " \
        if wild_campsite_nights else ""
    campground_nights_html = f"<i class='fas fa-campground' style='color: green;' data-bs-toggle='tooltip' data-bs-placement='top' title='campground'></i> {campground_nights}  &nbsp;" \
        if campground_nights else ""
    indoor_refuge_html = f"<i class='fa-solid fa-house' style='color: red;' data-bs-toggle='tooltip' data-bs-placement='top' title='refuge (free)'></i> {indoor_refuge} &nbsp; " \
        if indoor_refuge else ""
    indoor_unstaffed_html = f"<i class='fa-solid fa-house' style='color: orange;' data-bs-toggle='tooltip' data-bs-placement='top' title='unstaffed hut'></i> {indoor_unstaffed} &nbsp; " \
        if indoor_unstaffed else ""
    indoor_staffed_html = f"<i class='fa-solid fa-house' style='color: green;' data-bs-toggle='tooltip' data-bs-placement='top' title='staffed hut, B&B or hotel'></i> {indoor_staffed} &nbsp; " \
        if indoor_staffed else ""

    meta = f"<b>{kilometers}</b> km in <b>{days}</b> days. &nbsp; " if kilometers else ""

    overnights_html = meta + wild_rough_nights_html + wild_campsite_nights_html + campground_nights_html + \
                      indoor_refuge_html + indoor_unstaffed_html + indoor_staffed_html
    return mark_safe(overnights_html)