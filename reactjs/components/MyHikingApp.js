import React from 'react';

import MyHome from './MyHome';
import MyHikeList from './MyHikeList';
import MyAppBar from './MyAppBar';
import MyTabs from './MyTabs';
import MyButton from './MyButton';
import HikesScreen from '../containers/HikesScreen';

import { Link } from 'react-router'

const styles = {

  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  gridList: {
    width: 1500,
    height: 800,
    overflowY: 'auto',
  },
  gridTileStyle: {
    fontFamily: "Raleway",
    fontSize: 32,
  },
};

// encapsulate the Grid and the properties
// this.props.children is filled with the value from 'IndexRoute' in myIndex.js
class MyHikingApp extends React.Component {

    render() {
        return (
            <div>

                <ul className="header">

                </ul>
                <div className="content">
                    {this.props.children}
                </div>
            </div>
        )
    }
}

export default MyHikingApp;