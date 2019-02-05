from django.shortcuts import render
from django.http import HttpResponse
import json
from .modules.NonogramSolver import NonogramSolver


def index(request):
    return render(request, 'nonogramsolver/index.html')


def ajax(request):
    row_defs = json.loads(request.POST['row_defs'])
    col_defs = json.loads(request.POST['col_defs'])
    solver = NonogramSolver(row_defs, col_defs)
    return HttpResponse(json.dumps(solver.solve()))

