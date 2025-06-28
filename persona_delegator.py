# persona_delegator.py
# Purpose: Assign the best persona for the given task

from autonomy_router import route_task

def assign_persona(task_name):
    return route_task(task_name)