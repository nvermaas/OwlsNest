
import React from 'react'
import ReactDOM from 'react-dom'
import {render} from 'react-dom';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MyAwesomeReactComponent from './components/MyAwesomeReactComponent';
import MyMaterialExample from './components/MaterialExample';
import MyAppBarExample from './components/MyAppBar';

import injectTapEventPlugin from 'react-tap-event-plugin';
// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();

import HikeList from './components/HikeList';
import MyPrettyHikeList from './components/MyPrettyHikeList';

//var React = require('react')
//var ReactDOM = require('react-dom')
render(<MyAppBarExample />, document.getElementById('myHeaderContainer'));


ReactDOM.render(
  <MyAwesomeReactComponent />,
  document.getElementById('myMaterialContainer1')
);


ReactDOM.render(
    <MyPrettyHikeList url='/hiking/rest' pollInterval={5000} />,
    document.getElementById('myListContainer'));

//render(<MyMaterialExample />, document.getElementById('myMaterialContainer2'));
