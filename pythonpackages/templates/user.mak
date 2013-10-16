<%inherit file="root.mak"/>

<%block name="jumbotron">
    <h1>Profile</h1>
    <p>${user}</p>
    <p><a href="${auth_url}" class="btn btn-primary btn-lg">Connect to PyPI &raquo;</a></p>
</%block>

<%block name="content">
</%block>
