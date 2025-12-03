from fastapi import APIRouter, Request, Form
from src.utils import db
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory='templates')
router = APIRouter()


@router.get('/tasks')
def get_tasks(request: Request):
    res = db.table('tasks').select('*').execute()
    data = res.data
    return templates.TemplateResponse('home.html', {'request': request, 'tasks': data})


@router.get('/tasks/create')
def show_create_task_form(request: Request):
    return templates.TemplateResponse('create_task.html', {'request': request})


@router.post('/tasks/create')
def create_task(request: Request, title = Form(...), description = Form(...), status = Form(...)):
    data = {
        'title': title,
        'description': description,
        'status': status
    }
    res = db.table('tasks').insert(data).execute()
    return RedirectResponse('/tasks', status_code=302)

@router.get('/tasks/edit')
def show_update_form(request: Request, id):
    res = db.table('tasks').select('*').eq('id', id).execute()
    data = res.data
    return templates.TemplateResponse('update_task.html', {'request': request, 'task': data})



@router.post('/task/update')
def update_task(request: Request, id, title = Form(...), description = Form(...), status = Form(...)):
    data = {
        'title': title,
        'description': description,
        'status': status
    }
    res = db.table('tasks').update(data).eq('id', id).execute()
    return RedirectResponse('/tasks', status_code=302)

@router.get('/tasks/delete')
def delete_task(request: Request, id):
    res = db.table('tasks').delete().eq('id', id).execute()
    return RedirectResponse('/tasks', status_code=302)