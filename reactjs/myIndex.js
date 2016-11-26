
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
import MyHikeListGrid from './components/MyHikeListGrid';
import MyHikeListCards from './components/MyHikeListCards';
import MyPaperChild from './components/MyPaperChild'

render(<MyAppBarExample />, document.getElementById('myHeaderContainer'));

//render(<MyPaperChild />, document.getElementById('myPaperContainer'));


render(<MyAwesomeReactComponent />,document.getElementById('myMaterialContainer1'));


render(<MyHikeListGrid url='/hiking/rest' pollInterval={5000} />,document.getElementById('myListContainer'));

//render(<MyHikeListCards url='/hiking/rest' pollInterval={5000} />,document.getElementById('myListContainer'));

//render(<MyMaterialExample />, document.getElementById('myMaterialContainer2'));
