
import React from 'react'
import ReactDOM from 'react-dom'
import {render} from 'react-dom';
// import { Router, Route, Link, IndexRoute } from 'react-router'

import { createStore, applyMiddleware, combineReducers } from 'redux';
import { Provider, connect } from 'react-redux';

import thunk from 'redux-thunk';
import myStore from './myStore';

import MyHikingApp from './components/MyHikingApp';
import MyHikeList from './components/MyHikeList';
import MyHikeDetails from './components/MyHikeDetails';
import MyTabs from './components/MyTabs';

// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

var { Router,
      Route,
      IndexRoute,
      IndexLink,
      Link } = ReactRouter;


myStore.subscribe(() => {
    console.log("store changed", myStore.getState());
})

// examples of dispatch
//myStore.dispatch({type: "SET_HIKE_URL", payload: "nvermaas.xs4all.nl"});
//myStore.dispatch({type: "CHANGE_HIKE_ID", payload: 1});
//myStore.dispatch({type: "CHANGE_HIKE_ID", payload: 2});
//myStore.dispatch({type: "CHANGE_HIKE_YEAR", payload: 2017});


ReactDOM.render(
    <Provider store={myStore}>
        <Router>
           <Route path="/" component={MyHikingApp}>
               <IndexRoute component={MyTabs}/>
           </Route>
           <Route path="overview" component={MyHikeList}/>
           <Route path="details" component={MyHikeDetails}/>
     </Router>
     </Provider>,
    document.getElementById('myContainer')
 );
