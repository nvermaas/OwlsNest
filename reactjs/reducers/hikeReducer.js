
// this is the reducer for changing the hiking object
export function getSelectedHike(state) {
  return state.details;
}

const myHikeReducer = (state={}, action) => {
    console.log("hikeReducer(",action,")")
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
                    console.log("hikeReducer.data=", data);
                    console.log("hikeReducer.data.title=",data.title)
                    state = {...state, hike: data};

                    console.log("state.hike = ",state.hike);
                    console.log("state = "+state)
                }
            })
             console.log("state.hike = ",state.hike);
             console.log("state = "+state)
             break;
        }

        case "LOAD_ALL_FROM_SERVER": {
            var myUrl = action.payload;
            console.log("hikeReducer.loadAllFromServer(",myUrl,")")

            $.ajax({
                url: myUrl,
                datatype: 'json',
                cache: false,
                success: function(data) {
                    console.log(data);
                    state = {data: data};
                }
            })
             console.log("myHikeReducer.state: ",state);
             console.log("myHikeReducer.state.data = "+state.data)
             break;
        }
    }
    return state;
};

export default myHikeReducer;
