
//import React from 'react'
//import ReactDOM from 'react-dom'
import HikeList from './components/HikeList';

var React = require('react')
var ReactDOM = require('react-dom')


//ReactDOM.render(<HikeList url='/hiking/rest' pollInterval={5000} />,
//    document.getElementById('myMainContainer'))
ReactDOM.render(
    <h2>This is my Other Container</h2>,
    document.getElementById('myOtherContainer'));

//ReactDOM.render(
//    <HikeList url='/hiking/rest' pollInterval={5000} />,
//    document.getElementById('myContainer'));

ReactDOM.render(
    <HikeList url='/hiking/rest' pollInterval={5000} />,
    document.getElementById('myContainer'));
