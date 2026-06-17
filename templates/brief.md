# {{ brand_name }} - US Presence Brief

*Generated {{ generated_at }}*

## Summary

{% if brief %}
**Value proposition:** {{ brief.value_proposition}}

**Messaging consistency:** {{ brief.messaging_consistency }}

**US-presence signal:** {{brief.us_presence_signal }}

**Confidence:** {{ brief.confidence }}
{% else %}
_No brief has been generated for this brand yet._
{% endif %}


## Pages analyed

{% for page in pages %}
- [{{ page.title or page.url }}]({{ page.url }})
{% endfor %}