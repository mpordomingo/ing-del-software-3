from chronos.models import Task


class TaskController:

    @staticmethod
    def filter_by_code(code):
        task_set = Task.tasks.filter(code=code)
        assert len(task_set) <= 1
        if len(task_set) == 1:
            return task_set.first()
        else:
            return "No se econtro una tarea para ese codigo."

    @staticmethod
    def filter_by_description(description):
        task_set = Task.tasks.filter(description__contains=description)
        if len(task_set) > 0:
            return task_set
        else:
            return "No se encontraron tareas con esa descripcion."

    @staticmethod
    def filter_by_state(state):
        assert state in Task.valid_states()

        task_set = Task.tasks.filter(state=state)
        if len(task_set) > 0:
            return task_set
        else:
            return "No se encontraron tareas en ese estado."