<%inherit file="root.mak"/>

<%block name="nav">
    <li><a href="/">Home</a></li>
    <li class="active"><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
</%block>

<%block name="foo">
          <h1>About</h1>
          <br />

          <div class="row-fluid">
          <div class="span2"></div>
          <div class="span7"><img style="text-align: center" class="thumbnail" src="/static/img/python-packaging-pitch1.jpg"></div>
          </div>
          <br />
          <div class="row-fluid">
          <div class="span7"><img style="text-align: center" class="thumbnail" src="/static/img/python-packaging-pitch2.jpg"></div>
          <div class="span5"></div>
          </div>
          <br />

          <div class="row-fluid">
            <div class="span12" style="text-align: center">
                <img src="/static/img/pythonpackages-diagram.png">
            </div>
          </div>
          <br />
          <div class="row-fluid">
          <div class="span7"><img style="text-align: center" class="thumbnail" src="/static/img/python-packaging-pitch5.jpg"></div>
          <div class="span5"></div>
          </div>
          <br />
          <div class="row-fluid">
          <div class="span5"></div>
          <div class="span7"><img style="text-align: center" class="thumbnail" src="/static/img/python-packaging-pitch3.jpg"></div>
          </div>
          <br />
          <div class="row-fluid">
          <div class="span2"></div>
          <div class="span7"><img style="text-align: center" class="thumbnail" src="/static/img/python-packaging-pitch4.jpg"></div>
          </div>
</%block>
