from chronos.models import Task, TimeRecord


class TaskController:

    @staticmethod
    def filter_by_code(code):
        task_set = Task.tasks.filter(code=code)
        assert len(task_set) <= 1
        if len(task_set) == 1:
            return task_set.first()
        else:
            return "No se encontro una tarea para ese codigo."

    @staticmethod
    def filter_by_description(description):
        task_set = Task.tasks.filter(description__contains=description)
        if len(task_set) > 0:
            return task_set
        else:
            return "No se encontraron tareas con esa descripcion."

    @staticmethod
    def filter_by_state(state):
        assert state in Task.valid_states(), "El estado no es valido."

        task_set = Task.tasks.filter(state=state)
        if len(task_set) > 0:
            return task_set
        else:
            return "No se encontraron tareas en ese estado."

    @staticmethod
    def filter_by_title(title):
        task_set = Task.tasks.filter(title__contains=title)
        return task_set

    @staticmethod
    def filter_by_params(params):
        title = params.get('title', '')
        description = params.get('description', '')
        state = params.get('state', None)
        code = params.get('code', '')

        results = []

        tasks = Task.tasks.filter(title__icontains=title).filter(description__icontains=description)

        if state is not None:
            assert state in Task.valid_states(), "El estado no es valido."
            tasks = tasks.filter(state=state)

        if code is not "":
            tasks = tasks.filter(code=code)

        for task in tasks:
            responseTask = {}
            time_records = TimeRecord.records.filter(task_id=task.code)
            totalTime = 0
            workingTime = 0

            for record in time_records:
                totalTime += record.time_elapsed()
                workingTime += record.working_time()

            responseTask['totalTime'] = totalTime
            responseTask['workingTime'] = workingTime
            responseTask['code'] = task.code
            responseTask['title'] = task.title
            responseTask['state'] = task.state
            responseTask['description'] = task.description
            responseTask['totalRecords'] = len(time_records)
            results.append(responseTask)

        return results