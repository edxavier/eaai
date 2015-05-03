from django.db import models
from django.db import connection
from django.contrib.auth.models import User
from django.db.models import Count


class NotasManager(models.Manager):
	def status_Count(self):
		cursor=connection.cursor()
		query="select id,severity_id, COUNT(*) from bitacora_nota group by severity_id"
		cursor.execute(query)
		result=[]
		from .models import Severidad_nota 
		for row in cursor.fetchall():
			sev= Severidad_nota.objects.get(pk=row[1])#obtener la instancia de ese tipo de severidad
			n=self.model(id=row[0],severity=sev)
			n.total=row[2]
			result.append(n)
		return result

	def sist_statistics(self,inc):
		from bitacora.models import Nota
		return Nota.objects.values('systems__short_name').annotate(total=Count('systems')).filter(systems__gt=inc).order_by('-total')

	def Notas_por_Usuario_Count(self):
		from bitacora.models import Nota
		return Nota.objects.values('user__username').annotate(total=Count('user')).order_by('-total')
