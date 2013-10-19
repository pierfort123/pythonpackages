<%inherit file="root.mak" />

<%block name="jumbotron">

    <h1>Activity</h1>

</%block>

<%block name="content">
    <div class="row">
        <div class="col-lg-offset-4 col-lg-4">
          <h2>Logins</h2>
          <ul class="list-unstyled">
          % for entry in logged_in:
            <li><span class="glyphicon glyphicon-user"></span> ${link_user(entry.decode())|n}</li>
          % endfor
          </ul>
        </div>
    </div>
</%block>
