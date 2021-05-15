from .views import *
from datetime import datetime


class ForemanMainView(RoleRequiredView):
    user_role = 3
    form = None
    template_path = "wood_producing/foreman/foreman_main_view.html"

    def update_get_context(self, request, *args, **kwargs):
        task_name = request.GET.get("task_name")
        priority = request.GET.get("priority")
        status = request.GET.get("status")
        progress = request.GET.get("progress")
        due_date = request.GET.get("due")
        tasks = Task.objects.filter(userid=request.user)
        if task_name is not None and task_name != "":
            tasks = tasks.filter(name__contains=task_name)
        if priority is not None and priority != "":
            tasks = tasks.filter(priority=priority)
        if status is not None and status != "":
            tasks = tasks.filter(status=status)
        if progress is not None and progress != "":
            tasks = tasks.filter(progress__id=progress)
        if due_date is not None and due_date != "":
            day, month, year = due_date.split("/")
            tasks = tasks.filter(
                estimated__year=year,
                estimated__month=month,
                estimated__day=day
            )
        
        progress_list = Progress.objects.all()
        self.context["tasks"] = tasks
        self.context["progress_list"] = progress_list
        return None


class EditTaskView(RoleRequiredView):
    user_role = 3
    form = None
    template_path = "wood_producing/foreman/edit_task.html"

    def update_get_context(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        task = Task.objects.get(id=task_id)
        requested_materials = Materialrequest.objects.filter(taskid=task)
        for requested_material in requested_materials:
            pass
        self.context["task"] = task

        return None