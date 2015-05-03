# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import get_template
from .models import *
import datetime

class Nodes_boots(View):
    def get(self, request): 
        page_title = 'Gestion'
        page_sub_title= 'Historial de Reinicios' 
        boots = Boot_history.objects.order_by("-node_date")
        return render_to_response('gestion/boot_history.html', locals(),context_instance=RequestContext(request))

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Nodes_boots, self).dispatch(*args, **kwargs)
            
    def post(self,request,*args,**kwargs):
        try:
           # connect('gestion',host='192.168.137.200')
            #connect('gestion', host='mongodb://localhost/gestion')
            hist_entry = Boot_history()
            hist_entry.node = request.POST['node']
            hist_entry.platform = request.POST['platform']
            hist_entry.event = request.POST['event']
            hist_entry.node_date  = request.POST['date']
            hist_entry.server_date = datetime.datetime.now()
            hist_entry.save()
            return  HttpResponse("Post Saved")
        except Exception, e:
            return  HttpResponse("Error saving to DB"+ e.message)

       
class Host_list(View):
    def get(self, request): 
        page_title = 'Gestion'
        page_sub_title= 'Listado de equipos' 
        hosts = Hosts.objects
        return render_to_response('gestion/hosts.html', locals(),context_instance=RequestContext(request))        

class Host_cuadricula(View):
    def get(self, request): 
        page_title = 'Gestion'
        page_sub_title= 'Listado de equipos' 
        hosts = Hosts.objects
        return render_to_response('gestion/hosts_cuad.html', locals(),context_instance=RequestContext(request))        

class Host_details(View):
     def get(self, request,host_ip): 
        page_title = 'Gestion'
        page_sub_title= 'Detalles de ' + host_ip
        try:
            hosts = Hosts.objects(ip=host_ip)
            if hosts is not None:
                host= hosts[0]
            disks = Disk.objects(node_ip=host_ip)
            
            memories = Memory.objects(node_ip=host_ip)
            if len(memories)>0:
                memory = memories[0]
                uswap = memory.swap - memory.free_swap
            procs = Process.objects(node_ip=host_ip)
            loads = Load.objects(node_ip=host_ip)
            if len(loads)>0:
                load = loads[0]
            storages = Storage.objects(node_ip=host_ip)
            #devices = Device.objects(node_ip=host_ip)
            #sws = Software.objects(node_ip=host_ip)
            #interfaces = Interface.objects(node_ip=host_ip)

            return render_to_response('gestion/detalles.html', locals(),context_instance=RequestContext(request))        
        except Exception, e:
            return HttpResponse(e.message)

import json

class Json_data(View):
     def get(self, request,option,ip): 
        if option == "mem":
            re = Memory.objects(node_ip=ip).first()
            if re is not None:
                dic={'ram':re.ram,'used_ram':re.used_ram,'swap':re.swap,'free_swap':re.free_swap,'date':re.last_update.strftime('%d/%m/%Y %H:%M:%S')}
                return HttpResponse(json.dumps(dic,  indent=4),mimetype='application/json') 
            else:
                return HttpResponse("No data") 
        if option == "load":
            re = Load.objects(node_ip=ip).first()
            if re is not None:
                dic={'load':re.load_1}
                return HttpResponse(json.dumps(dic,  indent=4),mimetype='application/json') 
            else:
                return HttpResponse("No data")
        if option == "memh":
            res = Memory_hist.objects(node_ip=ip).order_by('date')
            dataset=[]
            for re in res:
                y = re.date.strftime('%Y')
                m = re.date.strftime('%m')
                d = re.date.strftime('%d')
                h = re.date.strftime('%H')
                mi = re.date.strftime('%M')
                dic={'mem_used':re.used_ram,'mem':re.ram,'year':y,'month':m,'day':d,'hour':h,'min':mi,}
                dataset.append(dic)
            return HttpResponse(json.dumps(dataset,  indent=4),mimetype='application/json') 
        if option == "loadh":
            res = Load_hist.objects(node_ip=ip).order_by('date')
            dataset=[]
            for re in res:
                year = re.date.strftime('%Y')
                month = re.date.strftime('%m')
                day = re.date.strftime('%d')
                hour = re.date.strftime('%H')
                mi = re.date.strftime('%M')
                dic={'load1':re.load1,'load5':re.load5,'load15':re.load15,'date':re.date.strftime('%d/%m/%Y %H:%M'),'year':year,'month':month,'day':day,'hour':hour,'min':mi}
                dataset.append(dic)
            return HttpResponse(json.dumps(dataset,  indent=4),mimetype='application/json') 
        if option == "diskh":
            if ip == "10.160.80.190" or ip == "10.160.80.191" or ip == "10.160.80.192":
                dpath = "/home/rec"
            else:
                dpath = "/"
            dhist = Disk_hist.objects(node_ip=ip,disk_path=dpath).order_by('date')
            dataset = []
            for h in dhist:
                year = h.date.strftime('%Y')
                month = h.date.strftime('%m')
                day = h.date.strftime('%d')
                hour = h.date.strftime('%H')
                mi = h.date.strftime('%M')
                dataset.append({ 'path':h.disk_path,'total':h.total, 'used':h.used,'year':year,'month':month,'day':day,'hour':hour,'min':mi})
            return HttpResponse(json.dumps(dataset,  indent=4),mimetype='application/json') 
        if option == "devices":
            devices = Device.objects(node_ip=ip)
            ds = []
            for device in devices:
                dic={'desc':device.desc,'status':device.status, 'date':device.last_update.strftime('%d/%m/%Y %H:%M:%S')}
                ds.append(dic)
            return HttpResponse(json.dumps(ds,  indent=4),mimetype='application/json') 
        if option == "sw":
            sws = Software.objects(node_ip=ip)
            ds = []
            for sw in sws:
                dic={'name':sw.name,'path':sw.path,'parameters':sw.parameters,'type':sw.type,'status':sw.status}
                ds.append(dic)
            return HttpResponse(json.dumps(ds,  indent=4),mimetype='application/json')
        if option == "procs":
            procs = Process.objects(node_ip=ip)
            ds = []
            for proc in procs:
                the_date = proc.last_update.strftime('%d/%m/%Y %H:%M:%S')
                flag = ""
                if proc.err_flag == 0:
                    flag = "<img src='/static/img/ok.png' style='width: 20px'>"
                else:
                    flag = "<img src='/static/img/warning.png' style='width: 20px'>"
                dic={'name':proc.name,'count':proc.count,'min':proc.minimun,'max':proc.maximun,'flag':flag,'err_msg':proc.err_msg,'date':the_date}
                ds.append(dic)
            return HttpResponse(json.dumps(ds,  indent=4),mimetype='application/json') 

        else:
            return HttpResponse("No valid option") 