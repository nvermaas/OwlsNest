import React from 'react';
import MyHome from './MyHome';
import MyHikeList from './MyHikeList';

// encapsulate the Grid and the properties
class MyHikingApp extends React.Component {

    render() {
        return (
            <div className="content">
                {this.props.children}
            </div>

        )
    }
}

export default MyHikingApp;