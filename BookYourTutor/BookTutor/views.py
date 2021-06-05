from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from BookTutor.serializers import TutorSerializer, \
    CustomerSerializer, \
    SubjectSerializer, \
    TutorSubjectSerializer, \
    TutorSubjectExtendedSerializer, \
    CustomerTutorSerializer, \
    SessionSerializer, \
    SessionCustomerSerializer, \
    TutorRatingSerializer, \
    ReviewSerializer, \
    InvoiceSerializer, \
    InvoiceSessionSerializer, \
    CustomerTutorExtendedSerializer, \
    TutorSubjectScheduleSerializer, TutorSubjectScheduleSerializerExtended

from django.forms.models import model_to_dict
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class LoginView(APIView):
    def post(self,request,format=None):
        user = authenticate(username=request.data["username"],password=request.data["password"])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            if request.data["type"]=="customer":
                customerObject = Customer.objects.filter(user__username__exact=user.username).values()
                print("Customer object: ",customerObject[0])

                if len(customerObject) > 0 :

                    userData = {
                        "id":customerObject[0]["id"],
                        "user_id": user.pk,
                        "username": user.username,
                        "email": user.email,
                        "name": customerObject[0]["name"],
                        "gender": customerObject[0]["gender"],
                        "city": customerObject[0]["city"],
                        "street": customerObject[0]["street"],
                        "contact": customerObject[0]["contact"],
                        "token": token.key,
                        "type":request.data["type"],
                    }
                    return Response(userData, status=status.HTTP_200_OK)
                else:
                    return  Response({"message": "No user found!"}, status=status.HTTP_404_NOT_FOUND)
            elif request.data["type"]=="tutor":
                tutorObject = Tutor.objects.filter(user__username__exact=user.username).values()
                print("tutorObject object: ", tutorObject[0])

                if len(tutorObject) > 0:

                    userData = {
                        "id": tutorObject[0]["id"],
                        "user_id": user.pk,
                        "username": user.username,
                        "email": user.email,
                        "name": tutorObject[0]["name"],
                        "gender": tutorObject[0]["gender"],
                        "city": tutorObject[0]["city"],
                        "street": tutorObject[0]["street"],
                        "contact": tutorObject[0]["contact"],
                        "token": token.key,
                        "type":request.data["type"]
                    }
                    return Response(userData, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "No user found!"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "No user found!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "No user found!"}, status=status.HTTP_404_NOT_FOUND)



class RegisterView(APIView):
    def post(self,request,format=None):
        # try:
        print(request.data)
        username=request.data["username"]
        email=request.data["email"]
        password=request.data["password"]

        if(username!="" and  email!="" and password!="" ):

            user=User.objects.create_user(username,email,password)

            userOtherData = {
                "name":request.data["name"],
                "gender":request.data["gender"],
                "city":request.data["city"],
                "street":request.data["street"],
                "contact":request.data["contact"],
                "user":user.pk,
            }
            if request.data["type"] == "customer":
                customerSerilazer = CustomerSerializer(data=userOtherData)
                if customerSerilazer.is_valid():
                    user.save()
                    customerSerilazer.save()
                    print("succesfully saved")
                    return Response(customerSerilazer.data, status=status.HTTP_201_CREATED)
                return Response(customerSerilazer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif request.data["type"] == "tutor":
                userSerilazer = TutorSerializer(data=userOtherData)
                print(userSerilazer)
                if userSerilazer.is_valid():
                    user.save()
                    userSerilazer.save()
                    print("succesfully saved")
                    return Response(userSerilazer.data, status=status.HTTP_201_CREATED)
                return Response(userSerilazer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Select user type!"}, status=status.HTTP_400_BAD_REQUEST)


        else:
            print("bad request")
            return Response({"message":"Enter all required fields!"}, status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     print(e)
        #     return Response({"message":"Error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TutorAsocSubjects(APIView):
    def get(self,request,tutorId):
        subjects = TutorSubject.objects.filter(tutorId__id__exact=tutorId)
        serializer = TutorSubjectExtendedSerializer(subjects, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,tutorId):
        subjects = {
            "name":request.data["name"],
            "code":request.data["code"],
            "address":request.data["address"],
            "level":request.data["level"]
        }
        subjectObj = Subject.objects.create(**subjects)
        # tutorObj=T.objects.get(id=tutorId)

        tutorSubject = {
            "tutorId" : Tutor.objects.get(id=tutorId),
            "subjectId" : subjectObj,
            "price":request.data["price"],
            "duration":int(request.data["duration"])
        }
        print(tutorSubject)
        tutorSubjectObj = TutorSubject.objects.create(**tutorSubject)
        tutorSerialzer = TutorSubjectSerializer(tutorSubjectObj)
        print(tutorSerialzer)




        return Response(tutorSerialzer.data,status=status.HTTP_201_CREATED)





# tutor crud api
class TutorListView(generics.ListCreateAPIView):
    serializer_class = TutorSerializer

    def get_queryset(self):
        return Tutor.objects.all()

class TutorDetailView (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TutorSerializer

    def get_queryset(self):
        return Tutor.objects.all()

# customer crud api
class CustomerListView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()

class CustomerDetailView (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()


# Subject crud api
class SubjectListView(generics.ListCreateAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()

# TutorSubject crud api
class TutorSubjectExtendedListView(APIView):

    def get(self, request,format=None):
        try:
            tutorSubjectList=[]
            tutors = Tutor.objects.all()
            for tutor in tutors:

                subjects = TutorSubject.objects.filter(tutorId__id__exact=tutor.id)
                serializer = TutorSubjectExtendedSerializer(subjects,many=True)
                tutorSubjectDict = {
                    **model_to_dict(tutor),
                    "subjects": [ subs["subjectId"] for subs in  serializer.data.copy() if "subjectId" in subs.keys()]


                }
                tutorSubjectList.append(tutorSubjectDict)




            return Response(tutorSubjectList)
        except Exception as e:
            print(e)
            return Response("Not found",status=status.HTTP_204_NO_CONTENT)


class TutorSubjectsSingleRow(APIView):
    def get(self,request):
        tutorsSubject = TutorSubject.objects.all()
        tutorsSubjectSerializer = TutorSubjectExtendedSerializer(tutorsSubject,many=True)
        return Response(tutorsSubjectSerializer.data,status=status.HTTP_200_OK)





class SubjectWiseTutorFilter(APIView):
    def get(self, request,subjectId, format=None):
        try:
            tutorSortLsit = TutorSubject.objects.filter(subjectId__id__exact = subjectId)
            tutorSubjectSerializer = TutorSubjectExtendedSerializer(tutorSortLsit,many=True)
            return Response(tutorSubjectSerializer.data)

        except Exception as e:
            return Response("Not found",status=status.HTTP_204_NO_CONTENT)

class SubjectFilterSearch(APIView):
    def get(self, request, subject,level,location, format=None):
        # try:
        print(subject,location)
        # getAddress= Subject.objects.get(id=location)
        tutorSearch = TutorSubject.objects.filter(subjectId__name__exact=subject).filter(subjectId__level__exact=level).filter(subjectId__address__exact=location)
        print(tutorSearch)
        tutorSubjectSerializer = TutorSubjectExtendedSerializer(tutorSearch, many=True)
        return Response(tutorSubjectSerializer.data)

        # except Exception as e:
        #     return Response("Not found",status=status.HTTP_204_NO_CONTENT)



class TutorSubjectListView(generics.ListCreateAPIView):
    serializer_class = TutorSubjectSerializer

    def get_queryset(self):
        return TutorSubject.objects.all()


class TutorSubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TutorSubjectSerializer

    def get_queryset(self):
        return TutorSubject.objects.all()



# CustomerTutor crud api
class CustomerTutorListView(generics.ListCreateAPIView):
    serializer_class = CustomerTutorSerializer

    def get_queryset(self):
        return CustomerTutor.objects.all()

    def post(self, request, *args, **kwargs):
        # 'customerId': userId.toString(),
        # 'tutorSubject': tutorSubjectId,
        customerTutor = CustomerTutor.objects.filter(customerId__id=request.data["customerId"],tutorSubject__id=request.data["tutorSubject"])
        if len(customerTutor) > 0:
            return Response({"message": "Already Added!"}, status=status.HTTP_208_ALREADY_REPORTED)
        else:
            customerTutorSerializer = CustomerTutorSerializer(data=request.data)
            if customerTutorSerializer.is_valid():
                customerTutorSerializer.save()
            else:
                return Response({"message": "Cannot Create"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(customerTutorSerializer.data, status=status.HTTP_201_CREATED)



class CustomerTutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerTutorSerializer

    def get_queryset(self):
        return CustomerTutor.objects.all()

# tutor subject schedule
class TutorSubjectScheduleListView(generics.ListCreateAPIView):
    serializer_class =TutorSubjectScheduleSerializer

    def get_queryset(self):
        return TutorSubjectSchedule.objects.all()

class TutorSubjectScheduleListViewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TutorSubjectScheduleSerializer

    def get_queryset(self):
        return TutorSubjectSchedule.objects.all()

class TutorScheduleSearch(APIView):
    def get(self,request,tutorSubjectId):
        tutorSchedules = TutorSubjectSchedule.objects.filter(tutorSubject__id =tutorSubjectId)
        tutorScheduleSerializer = TutorSubjectScheduleSerializer(tutorSchedules,many=True)
        return Response(tutorScheduleSerializer.data,status=status.HTTP_200_OK)

class TutorOnlyScheduleSearch(APIView):
    def get(self,request,tutorId):
        tutorSchedules = TutorSubjectSchedule.objects.filter(tutorSubject__tutorId__id=tutorId)
        tutorScheduleSerializer = TutorSubjectScheduleSerializerExtended(tutorSchedules,many=True)
        return Response(tutorScheduleSerializer.data,status=status.HTTP_200_OK)


# Session crud api
class SessionListView(generics.ListCreateAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        return Session.objects.all()


class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        return Session.objects.all()


# SessionCustomer crud api
class SessionCustomerListView(generics.ListCreateAPIView):
    serializer_class = SessionCustomerSerializer

    def get_queryset(self):
        return SessionCustomer.objects.all()


class SessionCustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SessionCustomerSerializer

    def get_queryset(self):
        return SessionCustomer.objects.all()

class AverageTutorRating(APIView):
    def get(self,request,tutorId):
        tutorRatings = TutorRating.objects.filter(tutorId__id=tutorId)
        ratings = []

        avgRatings=0
        if len(tutorRatings) > 0:
            for tutors in tutorRatings:
                ratings.append(float(tutors.rating))
            avgRatings = sum(ratings) / len(ratings)

        print(avgRatings)
        return Response({"averagerating":avgRatings},status=status.HTTP_200_OK)



# TutorRating crud api
class TutorRatingListView(generics.ListCreateAPIView):
    serializer_class = TutorRatingSerializer

    def get_queryset(self):
        return TutorRating.objects.all()


class TutorRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TutorRatingSerializer

    def get_queryset(self):
        return TutorRating.objects.all()


# Review crud api
class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


# Invoice crud api
class InvoiceListView(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.all()


# InvoiceSession crud api
class InvoiceSessionListView(generics.ListCreateAPIView):
    serializer_class = InvoiceSessionSerializer

    def get_queryset(self):
        return InvoiceSession.objects.all()


class InvoiceSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSessionSerializer

    def get_queryset(self):
        return InvoiceSession.objects.all()


# custom api's
class PriceTutorSort(APIView):
    def get(self,request,format=None):
        tutorSubject = TutorSubject.objects.all()
        orderby = request.query_params.get("orderby")

        if orderby:
            if orderby=="asc":
                tutorSubject = tutorSubject.order_by('price')
            elif orderby=="desc":
                tutorSubject = tutorSubject.order_by('-price')

            serializer = TutorSubjectExtendedSerializer(tutorSubject, many=True)
            # if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response({"message":"Error!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message":"Error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# booking list
class TutorSubjectBookings(APIView):
    def get(self,request,customerId):
        customerTutor = CustomerTutor.objects.filter(customerId__id=customerId)
        serialzer = CustomerTutorExtendedSerializer(customerTutor,many=True)
        return Response(serialzer.data,status=status.HTTP_200_OK)

class TutorBookingByTutor(APIView):
    def get(self,request,tutorId):
        customerTutor = CustomerTutor.objects.filter(tutorSubject__tutorId__id=tutorId)
        print(customerTutor)
        serialzer = CustomerTutorExtendedSerializer(customerTutor, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
