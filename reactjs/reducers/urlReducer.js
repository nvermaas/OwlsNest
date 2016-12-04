
// this is the reducer for changing the url
const myUrlReducer = (state={}, action) => {
    console.log("urlReducer")
    if (action.type == "SET_DETAILS_URL") {
        state = {...state, hiking_url: action.payload};
        console.log(action.type,' => ',state.hiking_url)
    }

   if (action.type == "GET_DETAILS_URL") {
    }
    return state;
};

export default myUrlReducer

