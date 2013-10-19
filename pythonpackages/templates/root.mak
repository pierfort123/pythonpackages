<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="https://github.com/pythonpackages/pythonpackages/blob/master/favicon.ico?raw=true">

    <title>Python Packages</title>

    <!-- Bootstrap core CSS -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-theme.min.css">

    <style>
        .navbar {
            background: #366C99;
        }
        /* Move down content because we have a fixed navbar that is 50px tall */
        body {
          padding-top: 50px;
          padding-bottom: 20px;
        }
    </style>

  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Python Packages</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <%block name="nav">
            <li class="active"><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
            </%block>
          </ul>
          <form class="navbar-right">
            % if not user:
            <a class="btn btn-success" style="color: white" href="${auth_url}">Sign in</a>
            % else:
            <ul class="list-unstyled">
                <li class="dropdown">
                    <a class="btn btn-success dropdown-toggle" data-toggle="dropdown" style="color: white" href="#">${user} <b class="caret"></b></a>
                    <ul class="dropdown-menu">
                        <li><a href="${user}">View profile</a></li>
                        <li><a href="/logout">Sign out</a></li>
                    </ul>
                </li>
            </ul>
            % endif
          </form>
        </div><!--/.navbar-collapse -->
      </div>
    </div>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <%block name="jumbotron">
        <h1>Hello, Python Programmers!</h1>
        <p>Python Packages connects your GitHub account to the Python Package Index to make publishing Python software easier and more fun.</p>
        <p><a href="/about" class="btn btn-primary btn-lg">Learn more &raquo;</a></p>
        </%block>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <%block name="content">
      <div class="row">
        <div class="col-lg-4">
          <h2><a href="/activity">Activity</a></h2>
          <ul class="list-unstyled">
          % for entry in logged_in:
            <li><span class="glyphicon glyphicon-user"></span> ${link_user(entry.decode())|n}</li>
          % endfor
          </ul>
        </div>
        <div class="col-lg-4">
          <h2>Heading</h2>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          <p><a class="btn btn-default" href="#">View details &raquo;</a></p>
       </div>
        <div class="col-lg-4">
          <h2>Heading</h2>
          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-default" href="#">View details &raquo;</a></p>
        </div>
      </div>
      </%block>

      <hr>

      <footer>
        <p>&copy; Company 2013</p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://code.jquery.com/jquery-2.0.3.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
