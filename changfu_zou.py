<!DOCTYPE HTML>
<html>

<head><script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setSiteSpeedSampleRate', 100]);</script>
    <meta charset="utf-8">

    <title>changfu_zou.py (editing)</title>
    <link rel="shortcut icon" type="image/x-icon" href="/ipynb/static/base/images/favicon.ico?v=30780f272ab4aac64aa073a841546240">
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <link rel="stylesheet" href="/ipynb/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=9b2c8d3489227115310662a343fce11c" type="text/css"/>
    <link rel="stylesheet" href="/ipynb/static/components/jquery-typeahead/dist/jquery.typeahead.min.css?v=7afb461de36accb1aa133a1710f5bc56" type="text/css"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="/ipynb/static/components/codemirror/lib/codemirror.css?v=2336fb49f85e9fa887ada9af35223dce">
<link rel="stylesheet" href="/ipynb/static/components/codemirror/addon/dialog/dialog.css?v=c89dce10b44d2882a024e7befc2b63f5">

    <link rel="stylesheet" href="/ipynb/static/style/style.min.css?v=919d6b8e09904fa50d95875519dcb45b" type="text/css"/>
    

    <link rel="stylesheet" href="/ipynb/custom/custom.css" type="text/css"/>
    <script src="/ipynb/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/ipynb/static/components/requirejs/require.js?v=6da8be361b9ee26c5e721e76c6d4afce" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20160607234429",
          
          baseUrl: '/ipynb/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/ipynb/custom',
            nbextensions : '/ipynb/nbextensions',
            kernelspecs : '/ipynb/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jquery: 'components/jquery/jquery.min',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/moment',
            codemirror: 'components/codemirror',
            termjs: 'components/term.js/src/term',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead'
          },
	  map: { // for backward compatibility
	    "*": {
		"jqueryui": "jquery-ui",
	    }
	  },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });
    </script>

    
    

</head>

<body class="edit_app " data-base-url="/ipynb/" data-file-path="changfu_zou.py">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed.
  </div>
</noscript>

<div id="header">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand pull-left"><a href="/ipynb/tree" title='dashboard'><img src='/ipynb/static/base/images/logo.png?v=7c4597ba713d804995e8f8dad448a397' alt='Jupyter Notebook'/></a></div>

  
  
  

    <span id="login_widget">
      
    </span>

  

  

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename"></span>
    <span class="last_modified"></span>
</span>


  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p class="navbar-text indicator_area">
          <span id="current-mode">current mode</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">File</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="#">New</a></li>
                <li id="save-file"><a href="#">Save</a></li>
                <li id="rename-file"><a href="#">Rename</a></li>
                <li id="download-file"><a href="#">Download</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="#">Find</a></li>
                <li id="menu-replace"><a href="#">Find &amp; Replace</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Key Map</li>
                <li id="menu-keymap-default"><a href="#">Default<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="#">Sublime Text<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">View</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
              <a href="#">Toggle Header</a></li>
              <li id="menu-line-numbers"><a href="#">Toggle Line Numbers</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Language</a>
              <ul id="mode-menu" class="dropdown-menu">
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"></div>
</div>


</div>






    



    <script src="/ipynb/static/edit/js/main.min.js?v=f64a723bb5ef9d2cbd60832671cbd509" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">if (window.parent == window) {var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-54743941-2']);_gaq.push(['_setDomainName', 'c-26d024943eac9052f8b6dd0a1103b532.resbaz.cloud.edu.au']);_gaq.push(['_setAllowLinker', true]);_gaq.push(['_trackPageview']);(function() {var ga = document.createElement('script'); ga.type = 'text/javascript';ga.async = true;ga.src = 'https://ssl.google-analytics.com/ga.js';var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(ga, s);})();}</script></body>

</html>