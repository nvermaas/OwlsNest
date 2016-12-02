export function setHikeUrl(url) {
   return {
       type : "SET_HIKE_URL",
       payload: {
           id: url,
       }
    }
}