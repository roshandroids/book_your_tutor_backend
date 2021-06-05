from django.contrib import admin
from . models import *

admin.site.register(Tutor)
admin.site.register(Customer)
admin.site.register(Subject)
admin.site.register(TutorSubject)
admin.site.register(CustomerTutor)
admin.site.register(SessionCustomer)
admin.site.register(TutorRating)
admin.site.register(Review)
admin.site.register(Invoice)
admin.site.register(InvoiceSession)
