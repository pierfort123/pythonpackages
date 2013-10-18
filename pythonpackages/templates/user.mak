<%inherit file="root.mak"/>

<%block name="jumbotron">
    <h1>Profile</h1>
    <p>${user}</p>
    % if has_permission:
    <p><a href="${access_token}" class="btn btn-primary btn-lg">Connect to PyPI &raquo;</a></p>
    % endif
</%block>

<%block name="content">
</%block>
