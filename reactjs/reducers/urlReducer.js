
// this is the reducer for changing the url
const myUrlReducer = (state={}, action) => {
    if (action.type == "SET_HIKE_URL") {
        state = {...state, hiking_url: action.payload};
        console.log(action.type,' => ',state.hiking_url)
    }

    return state;
};

export default myUrlReducer

