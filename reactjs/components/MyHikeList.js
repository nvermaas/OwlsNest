import React from 'react';
import MyHome from './MyHome';
import MyHikeListGrid from './MyHikeListGrid';
import MyAppBar from './MyAppBar';

// encapsulate the Grid and the properties
class MyHikeList extends React.Component {

    constructor(props) {
        console.log('MyHikeList constructor')
        super(props);
    }

    render() {
        return (
            <div>
                <MyAppBar />
                <MyHikeListGrid url='/hiking/rest' pollInterval={5000}></MyHikeListGrid>
            </div>

        )
    }
}

export default MyHikeList;