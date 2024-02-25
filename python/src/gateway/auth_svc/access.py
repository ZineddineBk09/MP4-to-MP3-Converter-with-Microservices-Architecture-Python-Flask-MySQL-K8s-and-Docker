import os, requests


def login(request):
    auth = request.authorization

    if not auth:
        return None, ("missing credentials", 401)

    basicAuth = (auth.username, auth.password)

    # use the login endpoint of the auth service
    response = requests.post(
        f"http://{os.environ['AUTH_SVC_ADDRESS']}/login", auth=basicAuth
    )

    if response.status_code != 200:
        return None, (response.text, response.status_code)

    return response.text, None
