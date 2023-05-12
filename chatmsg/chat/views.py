from django.shortcuts import render, redirect

def chatPage(request, *args, **kwargs):
    """
    Renders the chat page for the authenticated user.

    Args:
    - request (HttpRequest): the HTTP request sent by the client.
    - args: variable length argument list.
    - kwargs: arbitrary keyword arguments.

    Returns:
    - HttpResponse: the HTTP response to send back to the client.

    Example usage:
    - Add this view to your Django urls.py file and map it to a URL pattern, such as '/chat/'.
    """

    if not request.user.is_authenticated:
        return redirect("login-user")

    context = {}
    return render(request, "chat/chatPage.html", context)

