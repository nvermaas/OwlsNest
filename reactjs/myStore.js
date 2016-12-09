
import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from "redux-thunk"

// nv: could not find good CDN versions of this yet
//import promise from "redux-promise-middleware"
//import logger from "redux-logger"

import myReducers from "./reducers/myReducers"

console.log("initializing myStore...");

// an example of very simple middleware, which is executed every time
const logger =(store) => (next) => (action) => {
    console.log("action fired!", action);
    next(action);
}

//const myMiddleware = applyMiddleware(promise, thunk, logger());
const myMiddleware = applyMiddleware(thunk, logger);

const myStore = createStore(myReducers, myMiddleware);

export default myStore;
