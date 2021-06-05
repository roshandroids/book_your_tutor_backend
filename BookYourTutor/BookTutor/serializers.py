from rest_framework import serializers
from .models import *

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TutorSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSubject
        fields = '__all__'

class TutorSubjectExtendedSerializer(serializers.ModelSerializer):
    tutorId = TutorSerializer()
    subjectId = SubjectSerializer()
    class Meta:
        model = TutorSubject
        fields = '__all__'


class CustomerTutorExtendedSerializer(serializers.ModelSerializer):
    tutorSubject = TutorSubjectExtendedSerializer()
    customerId = CustomerSerializer()
    class Meta:
        model = CustomerTutor
        fields = '__all__'

class CustomerTutorSerializer(serializers.ModelSerializer):
    class Meta:
        customerId = CustomerSerializer()
        tutorSubject = TutorSubjectSerializer()
        model = CustomerTutor
        fields = '__all__'

class TutorSubjectScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorSubjectSchedule
        fields = '__all__'

class TutorSubjectScheduleSerializerExtended(serializers.ModelSerializer):
    tutorSubject = TutorSubjectExtendedSerializer()
    class Meta:
        model = TutorSubjectSchedule
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        subjectId = SubjectSerializer()
        tutorId = TutorSerializer()
        model = Session
        fields = '__all__'

class SessionCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        customer = CustomerSerializer()
        session = SessionSerializer()
        model = SessionCustomer
        fields = '__all__'

class TutorRatingSerializer(serializers.ModelSerializer):
    class Meta:
        customerId = CustomerSerializer()
        tutorId = TutorSerializer()
        model = TutorRating
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        customerId = CustomerSerializer()
        tutorId = TutorSerializer()
        model = Review
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        tutorCustomerId = CustomerTutorSerializer()
        model = Invoice
        fields = '__all__'

class InvoiceSessionSerializer(serializers.ModelSerializer):
    class Meta:
        session = SessionSerializer()
        customer = CustomerSerializer()
        model = InvoiceSession
        fields = '__all__'