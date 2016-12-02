
// this is the reducer for changing the hiking object

const myHikeReducer = (state={}, action) => {
    switch(action.type) {
        case "SET_HIKE_ID": {
            // state.hike.id = action.payload;  //wrong! state should be inmutable!
            state = {...state, id: action.payload};
            break;
        }

        case "SET_HIKE_YEAR": {
            state = {...state, year: action.payload};
            break;
        }

        case "LOAD_DETAILS_FROM_SERVER": {
            var myUrl = action.payload;
            console.log("hikeReducer.loadDetailsFromServer(",myUrl,")")

            $.ajax({
                url: myUrl,
                datatype: 'json',
                cache: false,
                success: function(data) {
                    console.log(data);
                    console.log(data.title)
                    state = {details: data};
                }
            })
             console.log("details: ",state);
             console.log("title = "+state.title)
             break;
        }
    }
    return state;
};

export default myHikeReducer;
