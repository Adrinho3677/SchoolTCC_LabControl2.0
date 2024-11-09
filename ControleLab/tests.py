from django.test import TestCase
import ControleLab.models as ctrl
import datetime as dt

# Create your tests here.

def test_relatorio():
    relatorios = ctrl.Relatorio.objects.all()

    for relatorio in relatorios:
        if relatorio.horario_devolucao == None and relatorio.numero.status == 'Indísponivel':
            print('ok')

    
def tests_horario_data():
    d = dt.date.today()
    data=d.strftime("%d/%m/%Y")
    print(data)

    horario_emprestimo=dt.datetime.now().strftime("%I:%M")
    print(horario_emprestimo)

test_relatorio()
tests_horario_data()