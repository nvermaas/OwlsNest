import { combineReducers } from "redux"
import myHikeReducer from "./hikeReducer"
import myUrlReducer from "./urlReducer"

const myReducers = combineReducers({
    hike        : myHikeReducer,
    hiking_url  : myUrlReducer,
 });

 export default myReducers;
