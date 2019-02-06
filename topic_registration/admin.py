from django.contrib import admin
from .models import Topic, Timer, TopicRegistration


class TopicAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ['name', 'professor']

    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
        if request.user.type == 'admin':
            return qs
        return qs.filter(professor=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.professor = request.user
        super().save_model(request, obj, form, change)


class TimerAdmin(admin.ModelAdmin):
    fields = ('start_date', 'end_date')


class TopicRegistrationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TopicRegistrationAdmin, self).get_queryset(request)
        if request.user.type == 'admin':
            return qs
        return qs.filter(student__professor=request.user)


admin.site.register(Topic, TopicAdmin)
admin.site.register(Timer, TimerAdmin)
admin.site.register(TopicRegistration, TopicRegistrationAdmin)
