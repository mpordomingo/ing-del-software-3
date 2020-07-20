from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chronos.models import *
from chronos.serializers import *
from django.http import HttpResponse
from chronos.controllers.taskController import TaskController
from time import time
from datetime import date
from datetime import datetime

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
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if len(tasks) == 0:
            return Response({"results": "SIN_RESULTADOS", "message": "No se encontraron resultados."})
        return Response({'results':  str(len(tasks)), 'tasks': tasks})

    elif request.method == 'POST':
        serializer = TaskCreationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"result": "ERROR", "message": "PARAMETROS_NO_VALIDOS", "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, code):
    """
    Retrieve, update or delete a code task.
    """

    tasks = Task.tasks.filter(code=code)
    if tasks.count() == 0:
        return Response({"message": "404. Tarea no encontrada."}, status=status.HTTP_404_NOT_FOUND)
    elif tasks.count() != 1:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    task = tasks.first()
    if request.method == 'GET':
        records = TimeRecord.records.filter(task_id=task.code)
        totalTime = 0
        workingTime = 0

        response = {}

        for record in records:
            totalTime += record.time_elapsed()
            workingTime += record.working_time()

        response['totalTime'] = totalTime
        response['workingTime'] = workingTime
        response['code'] = task.code
        response['title'] = task.title
        response['state'] = task.state
        response['description'] = task.description
        response['totalRecords'] = len(records)

        return Response(response)

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

            year = int(request.query_params.get('year', 0))
            month = int(request.query_params.get('month', 0))
            day = int(request.query_params.get('day', 0))
            aDate = date(year, month, day)

            wc = WorkCycle()
            rc = RestCycle()
            task.start()
            stime = datetime.now().time()
            time_record = TimeRecord(task=task, date=aDate, startTime=stime, workCycle=wc, restCycle=rc)
            wc.save()
            rc.save()
            time_record.save()
            task.save()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({"tr_code": time_record.code}, status=status.HTTP_200_OK)


@api_view(['GET'])
def pause_task(request, code):

    try:
        tr_code = int(request.query_params.get('trcode', None))
        time_record = TimeRecord.records.filter(code=tr_code).first()
    except TimeRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            time_record.stop()
            time_record.save()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def resume_task(request, code):
    try:
        task = Task.tasks.filter(code=code).first()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            year = int(request.query_params.get('year', 0))
            month = int(request.query_params.get('month', 0))
            day = int(request.query_params.get('day', 0))
            aDate = date(year, month, day)
            wc = WorkCycle()
            rc = RestCycle()
            stime=datetime.now().time()

            time_record = TimeRecord(task=task, date=aDate, startTime=stime, workCycle=wc, restCycle=rc)
            wc.save()
            rc.save()
            time_record.save()
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response({"tr_code": time_record.code}, status=status.HTTP_200_OK)


@api_view(['GET'])
def stop_task(request, code):

    try:
        tr_code = request.query_params.get('trcode', None)
        task = Task.tasks.filter(code=code).first()
        if tr_code is not None and int(tr_code) is not '-1':
            tr_code = int(tr_code)
            time_record = TimeRecord.records.filter(code=tr_code).first()
        else:
            time_record = None
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            if time_record is not None:
                time_record.ustop()
                time_record.save()
            task.finalize()
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


