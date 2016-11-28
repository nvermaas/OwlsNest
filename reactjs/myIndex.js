
import React from 'react'
import ReactDOM from 'react-dom'
import {render} from 'react-dom';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';


import injectTapEventPlugin from 'react-tap-event-plugin';
// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
injectTapEventPlugin();

import MyHikeListGrid from './components/MyHikeListGrid';
//import MyHikeListGrid from './components/MyHikeListGridBackup';

//import MyPaperChild from './components/MyPaperChild'
//render(<MyAwesomeReactComponent />,document.getElementById('myMaterialContainer1'));


//render(<MyHikeListGrid url='/hiking/rest' pollInterval={5000} />,document.getElementById('myListContainer'));
ReactDOM.render(
    <div>
        <MyHikeListGrid url='/hiking/rest' pollInterval={5000}></MyHikeListGrid>
    </div>,
    document.getElementById('myListContainer')
 );

//render(<MyMaterialExample />, document.getElementById('myMaterialContainer2'));
