import React from 'react';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import NavigationClose from 'material-ui/svg-icons/navigation/close';
import FlatButton from 'material-ui/FlatButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import ActionExplore from 'material-ui/svg-icons/action/explore';

function handleTouchTap() {
  alert('onTouchTap triggered on the title component');
}

function handleClick() {
  alert('click!');
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
const MyAppBarExample = () => (
  <MuiThemeProvider>
    <AppBar
        title={<span style={styles.title}>My Hiking Trips</span>}
        onTitleTouchTap={handleTouchTap}
        iconElementLeft={<IconButton><ActionExplore /></IconButton>}
        iconElementRight={<FlatButton label="Contact" />}
    />
  </MuiThemeProvider>
);

export default MyAppBarExample;