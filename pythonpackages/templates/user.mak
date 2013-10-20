<%inherit file="root.mak"/>

<%block name="jumbotron">
    <h1>Profile</h1>
    <p>${path}</p>
    % if has_permission(path, request.context, request):
    <p><a href="${access_token}" class="btn btn-primary btn-lg">Connect to PyPI &raquo;</a></p>
    % endif

    ${request.context}

</%block>

<%block name="content">
</%block>
