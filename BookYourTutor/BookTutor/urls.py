from django.urls import include, path
from . import views


urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register_user'),
    path('login', views.LoginView.as_view(), name='login'),

    path('tutor', views.TutorListView.as_view(), name='tutor_view'),
    path('tutor/<pk>', views.TutorDetailView.as_view(), name='tutor_detail'),

    path('customer', views.CustomerListView.as_view(), name='customer_view'),
    path('customer/<pk>', views.CustomerDetailView.as_view(), name='customer_detail'),

    path('subject', views.SubjectListView.as_view(), name='subject_view'),
    path('subject/<pk>', views.SubjectDetailView.as_view(), name='subject_detail'),

    path('tutorsubject', views.TutorSubjectListView.as_view(), name='tutorsubject_view'),
    path('tutorsubjectSingleRow', views.TutorSubjectsSingleRow.as_view(), name='tutorsubjectSinglRow'),
    path('tutorsubjectall', views.TutorSubjectExtendedListView.as_view(), name='tutorsubjectexpanded_view'),
    path('tutorsubject/<pk>', views.TutorSubjectDetailView.as_view(), name='tutorsubject_detail'),
    path('tutorsubjectfilter/<subjectId>', views.SubjectWiseTutorFilter.as_view(), name='tutorsubjectfilter'),
    path('tutorcustomsearch/<subject>/<level>/<location>', views.SubjectFilterSearch.as_view(), name='tutorcustomsearch'),

    path('tutorasocsub/<tutorId>', views.TutorAsocSubjects.as_view(), name='tutorasocsub'),


    path('bookings/<customerId>', views.TutorSubjectBookings.as_view(), name='bookings'),
    path('bookingsByTutor/<tutorId>', views.TutorBookingByTutor.as_view(), name='bookingsByTutor'),
    path('customertutor', views.CustomerTutorListView.as_view(), name='customertutor_view'),
    path('customertutor/<pk>', views.CustomerTutorDetailView.as_view(), name='customertutor_detail'),

    path('tutorScheduleSearch/<tutorSubjectId>', views.TutorScheduleSearch.as_view(), name='tutorSchedule_view'),
    path('tutorTimeTable/<tutorId>', views.TutorOnlyScheduleSearch.as_view(), name='tutorTimeTable'),
    path('tutorSchedule', views.TutorSubjectScheduleListView.as_view(), name='tutorSchedule_view'),
    path('tutorSchedule/<pk>', views.TutorSubjectScheduleListViewDetailView.as_view(), name='customertutor_detail'),

    path('session', views.SessionListView.as_view(), name='session_view'),
    path('session/<pk>', views.SessionDetailView.as_view(), name='session_detail'),

    path('sessioncustomer', views.SessionCustomerListView.as_view(), name='sessioncustomer_view'),
    path('sessioncustomer/<pk>', views.SessionCustomerDetailView.as_view(), name='sessioncustomer_detail'),

    path('tutoraverageRating/<tutorId>', views.AverageTutorRating.as_view(), name='tutoraverageRating'),
    path('tutorrating', views.TutorRatingListView.as_view(), name='tutorrating_view'),
    path('tutorrating/<pk>', views.TutorRatingDetailView.as_view(), name='tutorrating_detail'),

    path('review', views.ReviewListView.as_view(), name='review_view'),
    path('review/<pk>', views.ReviewDetailView.as_view(), name='review_detail'),

    path('invoice', views.InvoiceListView.as_view(), name='invoice_view'),
    path('invoice/<pk>', views.InvoiceDetailView.as_view(), name='invoice_detail'),

    path('invoicesession', views.InvoiceSessionListView.as_view(), name='invoicesession_view'),
    path('invoicesession/<pk>', views.InvoiceSessionDetailView.as_view(), name='invoicesession_detail'),

    path('pricesort', views.PriceTutorSort.as_view(), name='price_sort'),



]