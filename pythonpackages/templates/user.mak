<%inherit file="root.mak"/>

<%block name="jumbotron">
    <h1>Profile</h1>
    <p>${path}</p>
    % if has_permission(user, request.context, request):
    <p><a href="${access_token}" class="btn btn-primary btn-lg">Connect to PyPI &raquo;</a></p>
    % endif
</%block>

<%block name="content">
</%block>
