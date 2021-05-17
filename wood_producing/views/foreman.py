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
        task_history = Taskprogress.objects.filter(taskid=task)
        cur_time = datetime.now()
        setattr(task, "estimated", task.estimated.strftime('%m/%d/%Y'))
        add_at_str = ""
        update_at_str = ""
        newest_progress = None
        material_in_product = Materialinproduct.objects.filter(productid=task.orderedproductid.product)
        for material in material_in_product:
            taken_material = Materialrequest.objects.filter(taskid=task, is_approved=True)
            taken_material_ammount = 0
            if taken_material.first() is not None:
                for tm in taken_material:
                    taken_material_ammount += tm.quantity
            setattr(material, 'taken_material_ammount', taken_material_ammount)
            setattr(material, 'quantity_total', material.quantity * task.quantity)


        if len(task_history) > 0:
            newest_progress = task_history.last()
            setattr(newest_progress, "enddate", newest_progress.enddate.strftime('%m/%d/%Y'))
        if cur_time.month - int(task.create_at.strftime("%m")) > 0:
            add_at_str = "Added {} months ago".format(cur_time.month - int(task.create_at.strftime("%m")))
        elif cur_time.day - int(task.create_at.strftime("%d")) > 0:
            add_at_str = "Added {} days ago".format(cur_time.day - int(task.create_at.strftime("%d")))
        elif cur_time.hour - int(task.create_at.strftime("%H")) > 0:
            add_at_str = "Added {} hours ago".format(cur_time.hour - int(task.create_at.strftime("%H")))
        elif cur_time.minute - int(task.create_at.strftime("%M")) > 0:
            add_at_str = "Added {} minutes ago".format(cur_time.minute - int(task.create_at.strftime("%M")))

        if cur_time.month - int(task.update_at.strftime("%m")) > 0:
            update_at_str = "Updated {} months ago".format(cur_time.month - int(task.update_at.strftime("%m")))
        elif cur_time.day - int(task.update_at.strftime("%d")) > 0:
            update_at_str = "Updated {} days ago".format(cur_time.day - int(task.update_at.strftime("%d")))
        elif cur_time.hour - int(task.update_at.strftime("%H")) > 0:
            update_at_str = "Updated {} hours ago".format(cur_time.hour - int(task.update_at.strftime("%H")))
        elif cur_time.minute - int(task.update_at.strftime("%M")) > 0:
            update_at_str = "Updated {} minutes ago".format(cur_time.minute - int(task.update_at.strftime("%M")))
        
        progress = Progress.objects.all()
        self.context["task"] = task
        self.context["requested_materials"] = requested_materials
        self.context["task_history"] = task_history
        self.context["update_at_str"] = update_at_str
        self.context["add_at_str"] = add_at_str
        self.context["progress_list"] = progress
        self.context["newest_progress"] = newest_progress
        self.context["material_in_product"] = material_in_product
        return None

    def post(self, request, *args, **kwargs):
        priority = request.POST.get("priority")
        status = request.POST.get("status")
        progress = request.POST.get("progress")
        estimate_date = request.POST.get("estimate_date")
        done_percentage = request.POST.get("done_percentage")

        task_id = kwargs.get("task_id")
        task = Task.objects.get(id=task_id)
        task.priority = priority
        task.status = status

        task.save()
        list_progress = Taskprogress.objects.filter(taskid=task)
        cur_progress = None
        estimate_date_time = datetime.strptime(estimate_date, "%m/%d/%Y").date()
        if list_progress.first() is None:
            cur_progress = Taskprogress(
                progressid_id=progress, 
                taskid=task, 
                percentage=int(done_percentage),
                startdate=datetime.now(),
                enddate=estimate_date_time,
            )
            
            cur_progress.save()
        elif int(list_progress.first().progressid.id) != int(progress):
            cur_progress = Taskprogress(
                progressid_id=progress, 
                taskid=task, 
                percentage=int(done_percentage),
                startdate=datetime.now(),
                enddate=estimate_date_time,
            )
            
            cur_progress.save()
        else:
            cur_progress = list_progress.last()
            cur_progress.percentage = done_percentage
            cur_progress.enddate = estimate_date_time
            cur_progress.save()
        
        return HttpResponseRedirect("/foreman/edit_task/{}".format(task_id))



class TaskDetailView(RoleRequiredView):

    user_role = 3
    form = None
    template_path = "wood_producing/foreman/task_detail.html"

    def update_get_context(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        task = Task.objects.get(id=task_id)
        requested_materials = Materialrequest.objects.filter(taskid=task)
        task_history = Taskprogress.objects.filter(taskid=task)
        cur_time = datetime.now()
        setattr(task, "estimated", task.estimated.strftime('%m/%d/%Y'))
        add_at_str = ""
        update_at_str = ""
        newest_progress = None
        material_in_product = Materialinproduct.objects.filter(productid=task.orderedproductid.product)
        for material in material_in_product:
            taken_material = Materialrequest.objects.filter(taskid=task, is_approved=True)
            taken_material_ammount = 0
            if taken_material.first() is not None:
                for tm in taken_material:
                    taken_material_ammount += tm.quantity
            setattr(material, 'taken_material_ammount', taken_material_ammount)
            setattr(material, 'quantity_total', material.quantity * task.quantity)


        if len(task_history) > 0:
            newest_progress = task_history.last()
            setattr(newest_progress, "enddate", newest_progress.enddate.strftime('%m/%d/%Y'))
        if cur_time.month - int(task.create_at.strftime("%m")) > 0:
            add_at_str = "Added {} months ago".format(cur_time.month - int(task.create_at.strftime("%m")))
        elif cur_time.day - int(task.create_at.strftime("%d")) > 0:
            add_at_str = "Added {} days ago".format(cur_time.day - int(task.create_at.strftime("%d")))
        elif cur_time.hour - int(task.create_at.strftime("%H")) > 0:
            add_at_str = "Added {} hours ago".format(cur_time.hour - int(task.create_at.strftime("%H")))
        elif cur_time.minute - int(task.create_at.strftime("%M")) > 0:
            add_at_str = "Added {} minutes ago".format(cur_time.minute - int(task.create_at.strftime("%M")))

        if cur_time.month - int(task.update_at.strftime("%m")) > 0:
            update_at_str = "Updated {} months ago".format(cur_time.month - int(task.update_at.strftime("%m")))
        elif cur_time.day - int(task.update_at.strftime("%d")) > 0:
            update_at_str = "Updated {} days ago".format(cur_time.day - int(task.update_at.strftime("%d")))
        elif cur_time.hour - int(task.update_at.strftime("%H")) > 0:
            update_at_str = "Updated {} hours ago".format(cur_time.hour - int(task.update_at.strftime("%H")))
        elif cur_time.minute - int(task.update_at.strftime("%M")) > 0:
            update_at_str = "Updated {} minutes ago".format(cur_time.minute - int(task.update_at.strftime("%M")))
        
        progress = Progress.objects.all()
        self.context["task"] = task
        self.context["requested_materials"] = requested_materials
        self.context["task_history"] = task_history
        self.context["update_at_str"] = update_at_str
        self.context["add_at_str"] = add_at_str
        self.context["progress_list"] = progress
        self.context["newest_progress"] = newest_progress
        self.context["material_in_product"] = material_in_product
        return None