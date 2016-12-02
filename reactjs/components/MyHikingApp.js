import React from 'react';
import MyHome from './MyHome';
import MyHikeList from './MyHikeList';
import MyAppBarExample from './MyAppBar';
import MyButton from './MyButton';
import HikesScreen from '../containers/HikesScreen';

// encapsulate the Grid and the properties
class MyHikingApp extends React.Component {

    render() {
        return (
            <div>
                <MyAppBarExample />
                <MyButton title="first"/>
                <MyButton title="next"/>

                <div className="content">
                    {this.props.children}
                </div>
            </div>
        )
    }
}

export default MyHikingApp;