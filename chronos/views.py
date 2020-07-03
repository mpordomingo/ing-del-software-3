from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chronos.models import *
from chronos.serializers import TaskSerializer
from django.http import HttpResponse
from chronos.controllers.taskController import TaskController
from datetime import time
from datetime import date

def index(request):
    return HttpResponse("Bienvenido a Chronos App:)")


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all code tasks, or create a new task.
    """

    if request.method == 'GET':
        try:
            tasks = TaskController.filter_by_params(request.query_params)
        except Exception as e:
            return Response({"message":"Estado invalido"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, code):
    """
    Retrieve, update or delete a code task.
    """
    try:
        task = Task.tasks.filter(code=code).first()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            task.delete()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def start_task(request, code):

    try:
        task = Task.tasks.filter(code=code).first()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:

            hours = request.query_params.get('hours', 0)
            minutes = request.query_params.get('minutes', 0)
            seconds = request.query_params.get('seconds', 0)
            year =  int(request.query_params.get('year', 0))
            month = int(request.query_params.get('month', 0))
            day = int(request.query_params.get('day', 0))
            aDate = date(year, month, day)

            stime = time(int(hours), int(minutes), int(seconds))
            wc = WorkCycle()
            rc = RestCycle()
            task.start()
            time_record = TimeRecord(task=task, date=aDate, startTime=stime, workCycle=wc, restCycle=rc)
            wc.save()
            rc.save()
            time_record.save()
            task.save()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({"tr_code": time_record.code}, status=status.HTTP_200_OK)


@api_view(['GET'])
def pause_task(request, tr_code):

    try:
        time_record = TimeRecord.records.filter(code=tr_code)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            time_record.stop()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@api_view
def resume_task(request, code):
    try:
        task = Task.tasks.filter(code=code).first()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            hours = request.query_params.get('hours', 0)
            minutes = request.query_params.get('minutes', 0)
            seconds = request.query_params.get('seconds', 0)
            year = int(request.query_params.get('year', 0))
            month = int(request.query_params.get('month', 0))
            day = int(request.query_params.get('day', 0))
            aDate = date(year, month, day)

            stime = time(int(hours), int(minutes), int(seconds))
            wc = WorkCycle()
            rc = RestCycle()
            task.start()
            time_record = TimeRecord(task=task, date=aDate, startTime=stime, workCycle=wc, restCycle=rc)
            wc.save()
            rc.save()
            time_record.save()
            task.save()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({"tr_code": time_record.code}, status=status.HTTP_200_OK)


@api_view(['GET'])
def stop_task(request, code, tr_code):

    try:
        task = Task.tasks.filter(code=code).first()
        time_record = TimeRecord.records.filter(code=tr_code)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            time_record.ustop()
            task.finalize()
            time_record.save()
            task.save()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def delete_task(request):
    try:
        code = int(request.query_params.get('code'))
        task = Task.tasks.filter(code=code).first()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
           task.delete()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_200_OK)


