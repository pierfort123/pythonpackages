<%inherit file="root.mak"/>

<%block name="nav">
    <li><a href="/">Home</a></li>
    <li class="active"><a href="/about">About</a></li>
</%block>


<%block name="jumbotron">
    <h1>About Python Packages</h1>
    <p>Python Packages connects your GitHub account to the Python Package Index to make publishing Python software easier and more fun. This is a work in progress and you can help.</p>
    <p><a href="https://github.com/pythonpackages/pythonpackages" class="btn btn-primary btn-lg">Check out the code &raquo;</a></p>
</%block>


<%block name="content">

    <div class="alert alert-warning">
      <strong>Blocked</strong> Please note we are blocked waiting for an OAuth fix to PyPI. If you care, please add a comment to this ticket: <a href="https://bitbucket.org/pypa/pypi/issue/85/oauth-authorise-not-found-https-must-be">https://bitbucket.org/pypa/pypi/issue/85/oauth-authorise-not-found-https-must-be</a>.
    </div>

</%block>
