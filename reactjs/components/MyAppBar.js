import React from 'react';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import NavigationClose from 'material-ui/svg-icons/navigation/close';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import ActionExplore from 'material-ui/svg-icons/action/explore';

import { Link } from 'react-router'
import myStore from '../myStore';
import MyContactButton from './MyContactButton';
import MyHomeButton from './MyHomeButton';
import MyOverviewButton from './MyOverviewButton';
import MyDetailsButton from './MyDetailsButton';

function handleTouchTap() {
  console.log('onTouchTap triggered on the title component');
}

function handleClick() {
  console.log("MyAppBar.handleClick");

  // reload the hikinglist
  //var myUrl = "http://localhost:8000/hiking/rest"; // replace with redux selector and mapStateToProps
  //myStore.dispatch({type: "LOAD_ALL_FROM_SERVER", payload: myUrl});
}



const styles = {
  title: {
    cursor: 'pointer',
  },
};

/**
 * This example uses an [IconButton](/#/components/icon-button) on the left, has a clickable `title`
 * through the `onTouchTap` property, and a [FlatButton](/#/components/flat-button) on the right.
 */
const MyAppBar = () => (
  <MuiThemeProvider>
  <div>
    <AppBar
        title={<span style={styles.title}>My Hiking Trips</span>}
        onTitleTouchTap={handleClick}
        onClick={handleClick}
        iconElementLeft={<IconButton> <ActionExplore /></IconButton>}
      />

      <Link to="/overview" activeClassName="active"><RaisedButton label="Overview" /></Link>
      <Link to="/details" activeClassName="active"><RaisedButton label="Details" /></Link>
      <Link to="/contact" activeClassName="active"><MyContactButton myLabel = "Contact"/></Link>

  </div>
  </MuiThemeProvider>
);

export default MyAppBar;