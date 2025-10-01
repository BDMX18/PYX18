'''
Question: Access Control Decorator

Write a decorator @requires_permission(role) that:

Checks if the user has the required role (e.g., 'admin', 'editor', etc.)

If the user doesn't have permission, print: "Access Denied"

If the user does, run the function as normal.

Example:

current_user = {'name': 'John', 'role': 'viewer'}

@requires_permission('admin')
def delete_post():
    print("Post deleted.")

delete_post()


Output:

Access Denied
'''

user = {'name': 'John', 'role': 'admin'}

def requires_permission(required_role):
  def decorator(func):
    def innerDecorator():
      if user['role'] == required_role:
        func()
      else:
        print('Access Denied!')
    return innerDecorator
  return decorator

@requires_permission('admin')
def delete_post():
  print('Post Deleted!')

delete_post()