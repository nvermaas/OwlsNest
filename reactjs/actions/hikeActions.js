
export function setHikeId(id) {
   return {
       type : "SET_HIKE_ID",
       payload: {
           id: id,
       }
    }
}

export function setHikeYear(year) {
   return {
       type : "SET_HIKE_YEAR",
       payload: {
           id: year,
       }
    }
}

export function fetchHike() {
   return {
       type : "FETCH_HIKE",
       payload: {
           id: 1,
           title : "my hike",
           place : "my hiking place",
           country : "my hiking country",
           date : "my hiking date",
           year : "my hiking year",
       }
    }
}