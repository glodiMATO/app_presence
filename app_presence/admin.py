from django.contrib import admin
from app_presence.models import Grade
from app_presence.models import Fonction
from app_presence.models import Direction
from app_presence.models import Presence
from app_presence.models import Agent
from app_presence.models import Carte
from app_presence.models import Prestation
# Register your models here.


admin.site.register(Grade)
admin.site.register(Fonction)
admin.site.register(Direction)
admin.site.register(Presence)
admin.site.register(Agent)
admin.site.register(Carte)
admin.site.register(Prestation)
