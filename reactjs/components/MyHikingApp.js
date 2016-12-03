import React from 'react';

import MyHome from './MyHome';
import MyHikeList from './MyHikeList';
import MyAppBar from './MyAppBar';
import MyTabs from './MyTabs';
import MyButton from './MyButton';
import HikesScreen from '../containers/HikesScreen';

// encapsulate the Grid and the properties
// this.props.children is filled with the value from 'IndexRoute' in myIndex.js
class MyHikingApp extends React.Component {

    render() {
        return (
            <div>
                <MyAppBar />
                <div className="content">
                    {this.props.children}
                </div>
            </div>
        )
    }
}

export default MyHikingApp;