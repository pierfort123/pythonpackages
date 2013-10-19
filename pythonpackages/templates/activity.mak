<%inherit file="root.mak" />

<%block name="jumbotron">

    <h1>Activity</h1>

</%block>

<%block name="content">
    % for entry in logged_in:
    <div class="row">
        <div class="col-lg-12">
            <p><span class="glyphicon glyphicon-user"></span> ${link_user(entry.decode())|n}</p>
        </div>
    </div>
    % endfor
</%block>
