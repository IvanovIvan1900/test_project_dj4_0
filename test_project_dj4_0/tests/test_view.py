import pytest
from django.urls import reverse
from my_app.models import Client


@pytest.mark.django_db
def test_resolve_url_client_list():
    url = reverse('my_app:client_list')
    assert isinstance(url, str)


@pytest.mark.django_db
def test_factory(client_factory:Client):
    first_cleint = client_factory()
    two_client = client_factory()
    a = 4

# @pytest.mark.django_db
# def test_auth_view(auto_login_user):
#    client, user = auto_login_user()
#    url = reverse('my_timer:client_list')
#    response = client.get(url)
#    assert response.status_code == 200

# # @pytest.mark.django_db
# # def test_cli(user_1):
# #    assert True

# class TestWorkPlaceView:
#    def service_get_begin_date(self, date_inptu:datetime)->datetime:
#           return datetime.combine(date_inptu.date(), time(0,0,0), date_inptu.tzinfo)

#    def service_get_last_task(self, count_last_tasks:int,list_of_time_tracker:list[TimeTrack], dic_of_task:dict, curr_user:User,
#           clien_filter_id:int=None, task_name:str=None)->list[dict]:
#       my_now = datetime.now(pytz.utc)
#       list_of_result:list[dict] = []
#             # task_id
#             # max_date
#             # task_name
#             # task_is_acitve
#             # client_name
#             # client_id
#             # task_duration
#             # diff_day - сколько дней назад последний раз работали с задачей
#             # date_start_plan
#             # is_plan - это задача с датой начала
#             # is_outdate - это задача уже просрочена

#       array_track = [elem for elem in list_of_time_tracker if elem.user == curr_user and
#                      elem.task.is_active and
#                      (clien_filter_id is None or elem.task.client.id == clien_filter_id) and elem.task.client.is_active
#                      and (task_name is None or task_name in elem.task.name) 
#                      and not elem.is_delete
#                      ]
#       dic_of_timet_track:dict = {}
#       set_of_plan_task_wich_time_track =set()
#       for elem in array_track:
#          elem_data = dic_of_timet_track.get(elem.task.id, {})
#          elem_data["task"] = elem.task
#          elem_data["duration"] = elem_data.get("duration", 0) + elem.duration_sec
#          elem_data["max_date"] = elem.date_stop if elem_data.get("max_date", None) is None else  max(elem_data.get("max_date", None), elem.date_stop)
#          elem_data["duration_after_plan"] = elem_data.get("duration_after_plan", 0) + 0 if (elem.task.date_start_plan is None or elem.date_stop < elem.task.date_start_plan) else elem.duration_sec
#          dic_of_timet_track[elem.task.id] = elem_data
#          set_of_plan_task_wich_time_track.add(elem.task)
#       temp_list_track = []
#       for key, value in dic_of_timet_track.items():
#          temp_list_track.append({"task_id":value["task"].id, "max_date":value["max_date"], "task_name":value["task"].name, "task_is_acitve":value["task"].is_active, 
#                "client_name":value["task"].client.name, "client_id":value["task"].client.id, "task_duration":int(value["duration"]),
#                "diff_day":((self.service_get_begin_date(my_now)-self.service_get_begin_date(value["max_date"])).days), 
#                "date_start_plan":None if value["task"].date_start_plan is None else value["task"].date_start_plan.date()})
#       temp_list_track.sort(key=lambda time_track:time_track.get("max_date"), reverse=True)

#       array_of_all_task = [elem for elem in dic_of_task["task_all"] if elem.date_start_plan and elem.date_start_plan.date() <= my_now.date() and
#                elem.user==curr_user and
#                elem.is_active and 
#                (clien_filter_id is None or elem.client.id == clien_filter_id) and elem.client.is_active and 
#                (task_name is None or task_name in elem.name) and 
#                elem not in set_of_plan_task_wich_time_track
#                and not elem.is_delete]
#       array_of_all_task.sort(key=lambda task: task.date_start_plan, reverse=True)

#       for task in array_of_all_task:
#          list_of_result.append({"task_id":task.id, "max_date":None, "task_name":task.name, "task_is_acitve":task.is_active, 
#                "client_name":task.client.name, "client_id":task.client.id, "task_duration":0,
#                "diff_day":((self.service_get_begin_date(my_now)-self.service_get_begin_date(task.date_start_plan)).days), "date_start_plan":task.date_start_plan.date()})


#       list_of_result.extend(temp_list_track)
#       for elem in list_of_result:
#          elem_date = dic_of_timet_track.get(elem.get("task_id"))
#          elem['is_plan'] = False
#          elem['is_outdate'] = False
#          if elem['date_start_plan'] is not None and elem_date["duration_after_plan"] < 100:
#             elem['is_plan'] = True
#             if elem["date_start_plan"] < datetime.today().date() and elem_date["duration_after_plan"] < 100:
#                elem['is_outdate'] = True
#       list_of_result.sort(key=lambda elem:(not elem['is_plan'], elem['diff_day']))
#       return list_of_result[:count_last_tasks]

#    @pytest.mark.django_db
#    @pytest.mark.parametrize("curr_user, count_elem, task_name, my_client", [
#       (pytest.lazy_fixture("user_1"),None,None,None),
#       (pytest.lazy_fixture("user_1"),None,"act.1, client client 1",None),
#       (pytest.lazy_fixture("user_1"),None,"act.1, client client 1, user user_2",pytest.lazy_fixture("client_1")),
#       (pytest.lazy_fixture("user_2"),None,"act.1, client client 1, user user_2, date plan None, del.0",pytest.lazy_fixture("client_1")),
#       (pytest.lazy_fixture("user_1"),None,None,pytest.lazy_fixture("client_1")),
#       (pytest.lazy_fixture("user_1"),None,None,pytest.lazy_fixture("client_1")),
#       (pytest.lazy_fixture("user_1"),None,None,pytest.lazy_fixture("client_1")),
#       ])
#    def test_last_task_wichout_filter_succes(self, auto_login_user, get_list_of_time_tracker:list[TimeTrack], curr_user:User, 
#                task_list_of_task, count_elem:int, task_name:str, my_client:Clients):
#       if count_elem is None:
#              count_elem = Pref.get_pref_by_name('work_place_count_last_task', 10)
#       client_id = my_client.id if my_client else None
#       dic_of_param = {"search_button":"search"}
#       if my_client:
#          dic_of_param["client"] = client_id
#       if task_name:
#          dic_of_param["task_name"] = task_name
      
#       client, user = auto_login_user(curr_user)
#       url = reverse('my_timer:work_place')
#       response = client.get(url, dic_of_param)

#       assert response.status_code == 200

#       etalon_list = self.service_get_last_task(count_last_tasks=count_elem, list_of_time_tracker=get_list_of_time_tracker, 
#          dic_of_task=task_list_of_task, curr_user=curr_user, task_name=task_name, clien_filter_id=client_id)
      
#       get_list = response.context['array_dic_of_data_last_tasks']
#       assert len(etalon_list)==len(get_list)
#       for i in range(len(etalon_list)):
#              assert etalon_list[i]==get_list[i]
