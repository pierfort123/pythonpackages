<%inherit file="root.mak"/>

<%block name="nav">
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li class="active"><a href="/contact">Contact</a></li>
</%block>

<%block name="foo">
        <h1>Contact</h1>
        <p>We are here to help you package and release your Python software. Get in touch!</p>
</%block>
<%block name="bar">
    <div class="span9">
        <i class="icon-github icon-3x pull-left"></i><p>Our GitHub organization, which contains code for this website and other project-related repositories: <a href="https://github.com/pythonpackages">https://github.com/pythonpackages</a>.</p>
    </div>
</%block>
