
import React from 'react'
import ReactDOM from 'react-dom'
import {render} from 'react-dom';

import MyHikingApp from './components/MyHikingApp';
import MyHikeList from './components/MyHikeList';

import injectTapEventPlugin from 'react-tap-event-plugin';
// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();

var { Router,
      Route,
      IndexRoute,
      IndexLink,
      Link } = ReactRouter;


ReactDOM.render(
    <Router>
        <Route path="/" component={MyHikingApp}>
            <IndexRoute component={MyHikeList}/>
        </Route>
    </Router>,
    document.getElementById('myContainer')
 );
