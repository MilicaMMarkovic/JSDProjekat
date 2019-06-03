from os.path import join

from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
import pydot, os


def execute(path, grammar_file_name, example_file_name, export_dot, export_png):
    '''U svrhe brzeg testiranja, metoda koja prima putanju do foldera, naziv fajla gdje je gramatika i naziv fajla gdje je
        primjer programa u nasem jeziku i indikator da li da se eksportuju .dot i .png fajlovi'''

    meta_path = os.path.join(path, grammar_file_name)
    meta_path = path + '/' + grammar_file_name
    meta_name = os.path.splitext(meta_path)[0]
    metamodel = metamodel_from_file(meta_path)

    if export_dot:
        metamodel_export(metamodel, meta_name + '.dot')
        if export_png:
            graph = pydot.graph_from_dot_file(meta_name + '.dot')
            # graph[0].write_png(meta_name + '.png')

    model_path = path + '/' + example_file_name
    model_name = os.path.splitext(model_path)[0]
    model = metamodel.model_from_file(model_path)

    if export_dot:
        model_export(model, model_name + '.dot')
    if export_png:
        graph = pydot.graph_from_dot_file(model_name + '.dot')

    def function(model):
        string = 'from django.views import generic\nfrom django.views.generic.edit import CreateView, UpdateView, DeleteView\nfrom django.urls import reverse_lazy, reverse\n'
        string += '\n'
        for m in model:
            string += 'from .models import ' + m.name + '\n'

        for m in model:
            string += '\n'
            string += 'class ' + m.name + 'CreateView(CreateView):'
            string += '\n\t'
            string += 'template_name' + '=' + "'.html'" + '\n\t'
            string += 'model' + '=' + m.name + '\n\t'
            string += 'fields = ['
            last = len(m.modelElements) - 1
            for i, element in enumerate(m.modelElements):
                string += "'" + element.name + "'"
                if i == last:
                    string += ']'
                else:
                    string += ', '
            string += '\n\t' + "success_url=reverse_lazy('')"
            string += '\n\n'

            # Update
            string += '\n'
            string += 'class ' + m.name + 'UpdateView(UpdateView):'
            string += '\n\t'
            string += 'template_name' + '=' + "'.html'" + '\n\t'
            string += 'model' + '=' + m.name + '\n\t'
            string += 'fields = ['
            last = len(m.modelElements) - 1
            for i, element in enumerate(m.modelElements):
                string += "'" + element.name + "'"
                if i == last:
                    string += ']'
                else:
                    string += ', '
            string += '\n\n'

            # Delete
            string += '\n'
            string += 'class ' + m.name + 'DeleteView(DeleteView):'
            string += '\n\t'
            string += 'template_name' + '=' + "'.html'" + '\n\t'
            string += 'model' + '=' + m.name + '\n\t'
            string += "success_url=reverse_lazy('')"
            string += '\n\n'

            # Listview
            string += '\n'
            string += 'class ' + m.name + 'ListView(generic.ListView):'
            string += '\n\t'
            string += 'template_name' + ' = ' + "'.html'" + '\n\t'
            string += 'context_object_name' + ' = ' + "'" + 'all_' + m.name + "'" + '\n\t'
            string += 'def ' + 'get_queryset(self):' + '\n\t\t'
            string += 'return ' + m.name + '.object.all'
            string += '\n\n'
        return string

    with open(r'C:\Users\Mica\Desktop\JSDProjekat\core\views.py', 'w') as f:
        a = function(model.models)
        f.write(a)

    def functionM(model):
        string = 'import os\nfrom django.db import models\nfrom django.utils.timezone import now\n'
        string += '\n'
        for m in model:
            string += '\n'
            string += 'class ' + m.name + '(models.Model):\t'
            for i, element in enumerate(m.modelElements):
                string += '\n\t'
                string += element.name + " = " + "models."

                if element.elementType.foreignKey is not None:
                    string += 'ForeignKey(' + str.capitalize(element.name) + ', ' + 'on_delete=models.CASCADE)'
                elif element.elementType.charField is not None:
                    string += 'CharField('
                    if len(element.elementType.charField.parameters) == 0:
                        string += ")),"
                    elif len(element.elementType.charField.parameters) == 1:
                        if element.elementType.charField.parameters[0].max_length is not None:
                            string += 'max_length=' + element.elementType.charField.parameters[
                                0].max_length.number + "),"
                        if element.elementType.charField.parameters[0].null is not None:
                            string += 'null=' + element.elementType.charField.parameters[0].null.booleanValue + "),"
                    elif len(element.elementType.charField.parameters) == 3:
                        string += 'max_length=' + element.elementType.charField.parameters[0].max_length.number + ", "
                        string += 'null=' + element.elementType.charField.parameters[1].null.booleanValue + ", "
                        string += 'default=' + element.elementType.charField.parameters[2].default.defaultValue.number + \
                                  ")"
                    elif element.elementType.charField.parameters[0].max_length and \
                            element.elementType.charField.parameters[1].null is not None:
                        string += 'max_length=' + element.elementType.charField.parameters[0].max_length.number + ", "
                        string += 'null=' + element.elementType.charField.parameters[1].null.value + ")"
                elif element.elementType.emailField is not None:
                    string += 'EmailField('
                    if len(element.elementType.emailField.parameters) == 0:
                        string += ")"
                    elif len(element.elementType.emailField.parameters) == 1:
                        if element.elementType.emailField.parameters[0].max_length is not None:
                            string += 'max_length=' + element.elementType.emailField.parameters[
                                0].max_length.number + ')'
                    elif len(element.elementType.emailField.parameters) == 3:
                        string += 'max_length=' + element.elementType.emailField.parameters[0].max_length.number + ", "
                        string += 'null=' + element.elementType.emailField.parameters[1].null.booleanValue + ", "
                        string += 'default=' + element.elementType.emailField.parameters[
                            2].default.defaultValue.number + ')'
                elif element.elementType.integerField is not None:
                    string += 'IntegerField('
                    if (len(element.elementType.integerField.parameters)) == 0:
                        string += ")"
                    elif len(element.elementType.integerField.parameters) == 1:
                        if element.elementType.integerField.parameters[0].max_length is not None:
                            string += 'max_length=' + element.elementType.emailField.parameters[
                                0].max_length.number + ')'
                        if element.elementType.integerField.parameters[0].null is not None:
                            string += 'null=' + element.elementType.charField.parameters[0].null.booleanValue + ")"
                    elif len(element.elementType.integerField.parameters) == 2:
                        string += 'max_length=' + element.elementType.integerField.parameters[
                            0].max_length.number + ', '
                        string += 'null=' + element.elementType.integerField.parameters[1].null.booleanValue + ')'
                elif element.elementType.dateTimeField is not None:
                    string += 'DateTimeField('
                    if len(element.elementType.dateTimeField.parameters) == 0:
                        string += ")"
                    elif len(element.elementType.dateTimeField.parameters) == 1:
                        if element.elementType.dateTimeField.parameters[0].null is not None:
                            string += 'null=' + element.elementType.dateTimeField.parameters[
                                0].null.booleanValue + ')'
                        if element.elementType.dateTimeField.parameters[0].null is not None:
                            string += 'default=' + element.elementType.emailField.parameters[
                                0].default.defaultValue.number + ")"
                    elif len(element.elementType.dateTimeField.parameters) == 2:
                        string += 'null=' + element.elementType.dateTimeField.parameters[
                            0].null.booleanValue + ', '
                        string += 'default=' + element.elementType.dateTimeField.parameters[
                            1].default.defaultValue.timezone.var + ')'
        return string

    #   with open(join("C:\Users\Mica\Desktop\JSDProjekat", '\core\models.py'), 'w') as f:
    with open(r'C:\Users\Mica\Desktop\JSDProjekat\core\models.py', 'w') as f:
        a = functionM(model.models)
        f.write(a)

    def functionU(model):
        string = 'from django.conf.urls import url\nfrom . import views\n'
        string += '\n' + 'app_name = ' + "'" + 'core' + "'"
        string += '\n\nurlpatterns = [' + '\n\n'
        string += ']'
        return string

    with open(r'C:\Users\Mica\Desktop\JSDProjekat\core\urls.py', 'w') as f:
        a = functionU(model)
        f.write(a)

    newpath = r'templates'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    def functionB(model):
        string = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>{% block title %} JSD PROJEKAT {% endblock %}</title>\n<body>\n{% block body %}\n{% endblock %}\n</body>\n</html>'
        return string

    with open('templates/base.html', 'w') as f:
        a = functionB(model)
        f.write(a)

    def functionB(model):
        string = "{% extends 'base.html' %}\n{% block title %} Prva strana {% endblock %}\n{% block body %}\n{% endblock %}"
        return string

    with open('templates/index.html', 'w') as f:
        a = functionB(model)
        f.write(a)

    def functionA(model):
        string = 'from django.contrib import admin\n'
        string += 'from .models import '
        last = len(model.models) - 1
        for i, model in enumerate(model.models):
            string += model.name
            if i == last:
                string += '' + '\n'
            else:
                string += ', '
        string += '' + '\n'
        string += 'admin.site.register(' + model.name + ')\n'
        string += 'admin.site.register(' + model.name + ')\n'
        string += 'admin.site.register(' + model.name + ')\n'
        return string

    with open(r'C:\Users\Mica\Desktop\JSDProjekat\core\admin.py', 'w') as f:
        a = functionA(model)
        f.write(a)
